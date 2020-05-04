#  MIT License
#
#  Copyright (c) 2020 Parakoopa
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#
from typing import Optional, List

from explorerscript.antlr.ExplorerScriptParser import ExplorerScriptParser
from explorerscript.error import SsbCompilerError
from explorerscript.ssb_converting.compiler.compile_handlers.abstract import AbstractStatementCompileHandler
from explorerscript.ssb_converting.compiler.compile_handlers.atoms.integer_like import IntegerLikeCompileHandler
from explorerscript.ssb_converting.compiler.compile_handlers.blocks.switches.default_case_block import \
    DefaultCaseBlockCompileHandler
from explorerscript.ssb_converting.compiler.compile_handlers.blocks.switches.case_block import \
    CaseBlockCompileHandler
from explorerscript.ssb_converting.compiler.compile_handlers.blocks.switches.switch_header import \
    SwitchHeaderCompileHandler
from explorerscript.ssb_converting.compiler.utils import CompilerCtx, SsbLabelJumpBlueprint
from explorerscript.ssb_converting.ssb_data_types import SsbOperation
from explorerscript.ssb_converting.ssb_special_ops import OP_CASE_TEXT, OP_DEFAULT_TEXT, SsbLabel, OP_JUMP


class SwitchBlockCompileHandler(AbstractStatementCompileHandler):
    """Handles an entire switch block, with all it's cases."""
    def __init__(self, ctx, compiler_ctx: CompilerCtx):
        super().__init__(ctx, compiler_ctx)
        self._switch_header_handler: Optional[SwitchHeaderCompileHandler] = None
        self._case_handlers: List[CaseBlockCompileHandler] = []
        self._default_handler_index: int = -1
        self._default_handler: Optional[DefaultCaseBlockCompileHandler] = None

    def collect(self) -> List[SsbOperation]:
        self.ctx: ExplorerScriptParser.Switch_blockContext
        # 0. Prepare labels to insert
        default_start_label = SsbLabel(
            self.compiler_ctx.counter_labels(), -1  # todo: routine id is not set yet, but not used anyway.
        )
        end_label = SsbLabel(
            self.compiler_ctx.counter_labels(), -1  # todo: routine id is not set yet, but not used anyway.
        )
        default_jmp_to_case_block: Optional[SsbLabelJumpBlueprint] = None
        case_ops: List[SsbOperation] = []
        default_ops: List[SsbOperation] = []

        # 1. For each case: Generate and allocate case header op templates
        for h in self._case_handlers:
            h.set_end_label(end_label)
            if h.is_message_case:
                raise SsbCompilerError(f"A switch case must contain a list of statements (line {self.ctx.start.line}.")
            jmp_blueprint = h.get_header_jump_template()
            first = self.compiler_ctx.counter_ops.allocate(1)
            jmp_blueprint.set_index_number(first)

        # 2. Default block (first because default is after no case op branched)
        if self._default_handler:
            # 2a. If has operations: Collect default sub block ops
            self._default_handler.set_end_label(end_label)
            default_ops = self._default_handler.collect()
            # 2b. If no operations: Insert a jump blueprint for now, note it, and if it comes up later during 3b,
            #     process it like explained there.
            if len(default_ops) == 0:
                default_jmp_to_case_block = SsbLabelJumpBlueprint(
                    self.compiler_ctx, self.ctx,
                    OP_JUMP, []
                )
        else:
            # 2c. If no default: Create a default block with just one jump to end label
            default_ops = [self._generate_jump_operation(OP_JUMP, [], end_label)]
        # 3. For each case:
        cases_waiting_for_a_block = []
        default_waits = False
        i = -1
        for i, h in enumerate(self._case_handlers):
            if not h.has_sub_block_handlers():
                # 3b. Else: Jump to the block of the next case which has a block.
                cases_waiting_for_a_block.append(h)
            else:
                # 3a. If the case has operations: Collect case sub-block ops
                ops = h.collect()
                for h_waiting in cases_waiting_for_a_block:
                    h_waiting.set_processed_header_jumps(
                        [h_waiting.get_header_jump_template().build_for(h.get_start_label())]
                    )
                cases_waiting_for_a_block = []
                if default_waits:
                    default_waits = False
                    default_ops = [default_jmp_to_case_block.build_for(h.get_start_label())]
                case_ops += ops
            if default_jmp_to_case_block and i == self._default_handler_index:
                default_waits = True
        # 3c. Edge case: We expected a next case with ops, but got end of switch instead. Invalid!
        if len(cases_waiting_for_a_block) > 0 or default_waits:
            # ok either we ended to early, or the last condition is the default one:
            if i > - 1 and self._default_handler_index == i + 1:
                # ok, we just jump to the default case then, even though it's a bit pointless.
                for h_waiting in cases_waiting_for_a_block:
                    h_waiting.set_processed_header_jumps(
                        [h_waiting.get_header_jump_template().build_for(default_start_label)]
                    )
            else:
                raise SsbCompilerError(f"Unexpected switch end (line {self.ctx.start.line})")
        # 4. Build ops list
        header_ops = []
        for h in self._case_handlers:
            header_ops += h.get_processed_header_jumps()
        return header_ops + [default_start_label] + default_ops + case_ops + [end_label]

    def add(self, obj: any):
        if isinstance(obj, CaseBlockCompileHandler):
            self._case_handlers.append(obj)
            return
        if isinstance(obj, DefaultCaseBlockCompileHandler):
            if self._default_handler is not None:
                raise SsbCompilerError(f"A switch block can only have a single default case (line {self.ctx.start.line}")
            self._default_handler = obj
            self._default_handler_index = len(self._case_handlers)
            return
        if isinstance(obj, SwitchHeaderCompileHandler):
            self._switch_header_handler = obj
            return
        self._raise_add_error(obj)