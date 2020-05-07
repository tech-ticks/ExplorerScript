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
import json
from typing import Dict, Tuple, List, Union


class SourceMapPositionMark:
    """A position mark encoded in the source code of SSBScript / ExplorerScript."""
    def __init__(self, line_number: int, column_number: int, argument_idx: int,
                 name: str, x_offset: int, y_offset: int, x_relative: int, y_relative: int):
        self.line_number = line_number
        self.column_number = column_number
        self.argument_idx = argument_idx
        self.name = name
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.x_relative = x_relative
        self.y_relative = y_relative

    @property
    def x_with_offset(self) -> Union[int, float]:
        """
        Returns the x position with offset, in tiles, as float or int
        See also skytemple_files.script.ssa.position.
        """
        offset = 0
        if self.x_offset == 2 or self.x_offset == 3:
            offset = 0.5
        elif self.x_offset >= 4:
            offset = 2
        return self.x_relative + offset

    @property
    def y_with_offset(self) -> Union[int, float]:
        """
        Returns the x position with offset, in tiles, as float or int
        See also skytemple_files.script.ssa.position.
        """
        offset = 0
        if self.y_offset == 2 or self.y_offset == 3:
            offset = 0.5
        elif self.y_offset >= 4:
            offset = 2
        return self.y_relative + offset

    def __str__(self):
        return f'SourceMapPositionMark<' \
               f'"{self.name}" @{self.line_number}:{self.column_number}:{self.argument_idx} - ' \
               f'{self.x_relative}:{self.x_offset}, {self.y_relative}:{self.y_offset}>)'

    def __eq__(self, other):
        if not isinstance(other, SourceMapPositionMark):
            return False
        return self.line_number == other.line_number and \
                self.column_number == other.column_number and \
                self.argument_idx == other.argument_idx and \
                self.name == other.name and \
                self.x_offset == other.x_offset and \
                self.y_offset == other.y_offset and \
                self.x_relative == other.x_relative and \
                self.y_relative == other.y_relative

    def serialize(self) -> str:
        return json.dumps([
            self.line_number, self.column_number, self.argument_idx,
            self.name, self.x_offset, self.y_offset, self.x_relative, self.y_relative
        ])

    @classmethod
    def deserialize(cls, json_str: str) -> 'SourceMapPositionMark':
        json_d = json.loads(json_str)
        return SourceMapPositionMark(
            line_number=json_d[0], column_number=json_d[1], argument_idx=json_d[2],
            name=json_d[3], x_offset=json_d[4], y_offset=json_d[5], x_relative=json_d[6], y_relative=json_d[7]
        )


class SourceMap:
    """
    A source map for ExplorerScript and SSBScript back to the SSB binary opcodes.
    Takes a routine id and opcode index and returns the line in the source code, that this
    operation is at.

    The mapped addresses are the addresses relative to the first routine opcode address.

    Can be created in the following ways:
    - When loading SSB:
      - For SSBScript:
        - During decompilation.
      - For ExplorerScript:
        - Either during the decompilation, if no ExplorerScript exists yet.
        - From an existing source map file.
    - When compiling SSBScript or ExplorerScript the source map is also generated.

    This also provides information about position marks used in the source file.
    """
    def __init__(self, mappings: Dict[int, Tuple[int, int]], position_marks: List[SourceMapPositionMark]):
        """Init from a dictionary of mappings
        (keys are routine ids, values are dict of line numbers + column for opcodes)"""
        self._mappings = mappings
        self.position_marks = position_marks

    def get_position(self, op_offset: int) -> Tuple[int, int]:
        if op_offset in self._mappings:
            return self._mappings[op_offset]

    def __iter__(self):
        for opcode_offset, (line_number, column) in self._mappings.items():
            yield opcode_offset, line_number, column

    def __eq__(self, other):
        if not isinstance(other, SourceMap):
            return False
        return self._mappings == other._mappings and self.position_marks == other.position_marks

    def serialize(self) -> str:
        return json.dumps({
            'map': self._mappings,
            'pos_marks': [m.serialize() for m in self.position_marks]
        })

    @classmethod
    def deserialize(cls, json_str: str) -> 'SourceMap':
        json_d = json.loads(json_str)
        return SourceMap(
            {x: (y[0], y[1]) for x, y in json_d['map'].items()},
            [SourceMapPositionMark.deserialize(m) for m in json_d['pos_marks']]
        )


class SourceMapBuilder:
    def __init__(self):
        self._mappings = {}
        self._pos_marks = []

    def add_opcode(self, op_offset, line_number, column):
        self._mappings[op_offset] = (line_number, column)

    def add_position_mark(self, position_mark: SourceMapPositionMark):
        self._pos_marks.append(position_mark)

    def build(self):
        return SourceMap(self._mappings, self._pos_marks)
