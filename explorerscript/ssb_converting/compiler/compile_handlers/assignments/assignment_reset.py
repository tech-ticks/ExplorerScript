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

from typing import List, Optional

from explorerscript.error import SsbCompilerError
from explorerscript.ssb_converting.compiler.compile_handlers.abstract import AbstractAssignmentCompileHandler
from explorerscript.ssb_converting.compiler.compile_handlers.atoms.scn_var import ScnVarCompileHandler
from explorerscript.ssb_converting.compiler.utils import CompilerCtx
from explorerscript.ssb_converting.ssb_data_types import SsbOperation, SsbOpParam
from explorerscript.ssb_converting.ssb_special_ops import OPS_FLAG__CLEAR, OPS_FLAG__RESET_DUNGEON_RESULT, \
    OPS_FLAG__RESET_SCENARIO


class AssignmentResetCompileHandler(AbstractAssignmentCompileHandler):
    def __init__(self, ctx, compiler_ctx: CompilerCtx):
        super().__init__(ctx, compiler_ctx)
        self.scn_var_target: Optional[SsbOpParam] = None

    def collect(self) -> List[SsbOperation]:
        if self.scn_var_target is None and not self.ctx.DUNGEON_RESULT():
            raise SsbCompilerError("No target for reset.")

        if self.ctx.DUNGEON_RESULT():
            return [self._generate_operation(OPS_FLAG__RESET_DUNGEON_RESULT, [])]

        return [self._generate_operation(OPS_FLAG__RESET_SCENARIO, [self.scn_var_target])]

    def add(self, obj: any):
        if isinstance(obj, ScnVarCompileHandler):
            self.scn_var_target = obj.collect()
            return

        self._raise_add_error(obj)
