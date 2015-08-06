# -*- coding: utf-8 -*-
# This file is part of the gunyanza.
# Copyright (C) 2014- Erik Bernhardsson
# Copyright (C) 2015- Tasuku SUENAGA <tasuku-s-github@titech.ac>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals, print_function

import numpy
import shogi

def board2arrays(b, flip=False):
    # 9 * 9 + 持ち駒 7 types * 2 color
    x = numpy.zeros(9 * 9 + 7 * 2, dtype=numpy.int8)

    # 駒をマスに配置
    for pos, piece in enumerate(b.pieces):
        if piece != shogi.NONE:
            color = int(bool(b.occupied[shogi.BLACK] & shogi.BB_SQUARES[pos]))
            col = int(pos % 9)
            row = int(pos / 9)
            if flip:
                row = 8 - row
                color = 1 - color

            piece = color * len(shogi.PIECE_TYPES) + piece

            x[row * 9 + col] = piece

    # 持ち駒それぞれの数を保存
    for color in shogi.COLORS:
        for piece_type in range(shogi.PAWN, shogi.KING):
            # 駒のタイプは1オリジンなので1引く
            x[81 + color * 7 + (piece_type - 1)] = b.pieces_in_hand[color].get(piece_type, 0)

    return x

def boardarrays2bitarray(board_arrays):
    # 駒は、1-14(先手)と16-29(後手)。
    # それぞれの駒の数値かどうかを0, 1の配列にして、hstackでつなげる。
    return numpy.hstack(numpy.array([
        (board_arrays[...,:81]==1).astype(int),
        (board_arrays[...,:81]==2).astype(int),
        (board_arrays[...,:81]==3).astype(int),
        (board_arrays[...,:81]==4).astype(int),
        (board_arrays[...,:81]==5).astype(int),
        (board_arrays[...,:81]==6).astype(int),
        (board_arrays[...,:81]==7).astype(int),
        (board_arrays[...,:81]==8).astype(int),
        (board_arrays[...,:81]==9).astype(int),
        (board_arrays[...,:81]==10).astype(int),
        (board_arrays[...,:81]==11).astype(int),
        (board_arrays[...,:81]==12).astype(int),
        (board_arrays[...,:81]==13).astype(int),
        (board_arrays[...,:81]==14).astype(int),
        (board_arrays[...,:81]==16).astype(int),
        (board_arrays[...,:81]==17).astype(int),
        (board_arrays[...,:81]==18).astype(int),
        (board_arrays[...,:81]==19).astype(int),
        (board_arrays[...,:81]==20).astype(int),
        (board_arrays[...,:81]==21).astype(int),
        (board_arrays[...,:81]==22).astype(int),
        (board_arrays[...,:81]==23).astype(int),
        (board_arrays[...,:81]==24).astype(int),
        (board_arrays[...,:81]==25).astype(int),
        (board_arrays[...,:81]==26).astype(int),
        (board_arrays[...,:81]==27).astype(int),
        (board_arrays[...,:81]==28).astype(int),
        (board_arrays[...,:81]==29).astype(int),
    ]))
