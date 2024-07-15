#  MIT License
#
#  Copyright (c) 2020-2024 Capypara and the SkyTemple Contributors
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
from __future__ import annotations

from explorerscript.error import SsbCompilerError
from explorerscript.ssb_converting.compiler.compile_handlers.abstract import (
    AbstractStatementCompileHandler,
    AbstractComplexBlockCompileHandler,
    AbstractComplexStatementCompileHandler,
)
from explorerscript.ssb_converting.compiler.compile_handlers.atoms.string import StringCompileHandler
from explorerscript.ssb_converting.compiler.utils import CompilerCtx
from explorerscript.ssb_converting.ssb_data_types import SsbOperation, SsbOpParam
from explorerscript.ssb_converting.ssb_special_ops import SsbLabel, OP_JUMP, SsbLabelJump
from explorerscript.util import _
from explorerscript_parser import ExplorerScriptParser, Antlr4ParserRuleContext


class DefaultCaseBlockCompileHandler(
    AbstractComplexBlockCompileHandler[
        ExplorerScriptParser.DefaultContext,
        "AbstractStatementCompileHandler[Antlr4ParserRuleContext] | StringCompileHandler",
    ]
):
    """Handles a default block."""

    def __init__(self, ctx: ExplorerScriptParser.DefaultContext, compiler_ctx: CompilerCtx):
        super().__init__(ctx, compiler_ctx)
        self._added_string_handler: StringCompileHandler | None = None
        self.is_message_case = False
        # The end of the switch
        self._end_label: SsbLabel | None = None

    def set_end_label(self, end_label: SsbLabel) -> None:
        self._end_label = end_label

    def collect(self) -> list[SsbOperation]:
        if self.is_message_case:
            raise SsbCompilerError(_("Invalid message switch case call."))
        self.compiler_ctx.add_switch_case(self)
        retval = self._process_block(False)
        self.compiler_ctx.remove_switch_case()
        return retval

    def break_case(self) -> SsbLabelJump:
        return self._generate_jump_operation(OP_JUMP, [], self._end_label)

    def has_sub_block_handlers(self) -> bool:
        return len(self._added_handlers) > 0

    def get_text(self) -> SsbOpParam:
        assert self._added_string_handler is not None
        if not self.is_message_case:
            raise SsbCompilerError(_("Invalid message switch case call."))
        return self._added_string_handler.collect()

    def add(self, obj: AbstractStatementCompileHandler[Antlr4ParserRuleContext] | StringCompileHandler) -> None:
        if isinstance(obj, AbstractComplexStatementCompileHandler):
            # Sub statement for the block
            # WARNING: Might not have any operations. In this case, it's part of the following cases!
            self._added_handlers.append(obj)
            return
        if isinstance(obj, StringCompileHandler):
            # This is a case for a message switch.
            self.is_message_case = True
            self._added_string_handler = obj
            return
        self._raise_add_error(obj)
