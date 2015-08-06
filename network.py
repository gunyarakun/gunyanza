#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of the gunyanza.
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

import numpy as np
from chainer import cuda, Function, FunctionSet, gradient_check, Variable, optimizers
import chainer.functions as F

from utils import boardarrays2bitarray

def as_mat(x):
    return x.reshape(x.shape[0], x.size // x.shape[0])

class GunyaNetwork(FunctionSet):
  def __init__(self):
    super(GunyaNetwork, self).__init__(
        ## 9 x 9 board, convolution
        # l_board_conv_1=F.Convolution2D(14 * 2, 9, 3, pad=1),
        # l_board_conv_2=F.Convolution2D(9, 9, 3, pad=1),
        # l_board_conv_3=F.Convolution2D(9, 9, 3, pad=1),

        ## 9 x 9 board, suji/dan convolution
        # l_board_suji_1=F.Convolution2D(14 * 2, 9, (9, 1)),
        # l_board_dan_1=F.Convolution2D(14 * 2, 9, (1, 9)),

        l_2=F.Linear(14 * 2 * 9 * 9 + 7 * 2, 4096),
        l_3=F.Linear(4096, 4096),
        l_4=F.Linear(4096, 4096),
        l_5=F.Linear(4096, 1),
    )

  def forward(self, x_data, use_gpu, train=True):
    # board data is reshaped for convolution
    bitarrays = boardarrays2bitarray(x_data)
    board = bitarrays.reshape((-1, 14 * 2, 9, 9)) # num, color(piece_type), width, height
    piece = x_data[...,81:]

    if use_gpu:
        board = cuda.to_gpu(board.astype('float32'))
        piece = cuda.to_gpu(piece.astype('float32'))

    x = Variable(board, volatile=not train)
    p = Variable(piece, volatile=not train)

    # h_board_conv_1 = F.relu(self.l_board_conv_1(x))
    # h_board_conv_2 = F.relu(self.l_board_conv_2(h_board_conv_1))
    # h_board_conv_3 = F.relu(self.l_board_conv_3(h_board_conv_2))
    # h_board_conv_3_reshaped = Variable(as_mat(h_board_conv_3.data), volatile=not train)

    # h_board_suji_1 = F.relu(self.l_board_suji_1(x))
    # h_board_suji_1_reshaped = Variable(as_mat(h_board_suji_1.data), volatile=not train)
    # h_board_dan_1 = F.relu(self.l_board_dan_1(x))
    # h_board_dan_1_reshaped = Variable(as_mat(h_board_dan_1.data), volatile=not train)

    h_board_orig = Variable(as_mat(x.data), volatile=not train)

    ## Convolution 3x3, Convolution suji, Convolution dan, Original board, Pieces(Mochigomas)
    #h_1 = F.concat((h_board_conv_3_reshaped, h_board_suji_1_reshaped, h_board_dan_1_reshaped, h_board_orig, p))
    h_1 = F.concat((h_board_orig, p))
    h_2 = F.relu(self.l_2(h_1))
    h_3 = F.relu(self.l_3(h_2))
    h_4 = F.relu(self.l_4(h_3))
    h_5 = self.l_5(h_4)

    return h_5
