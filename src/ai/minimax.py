import random
import copy

from time import time

from src.constant import GameConstant, ShapeConstant
from src.model import State, Board

from typing import Tuple, List

from src.utility import *


class MinimaxGroup33:
    def __init__(self):
        pass

    def find(self, state: State, n_player: int, thinking_time: float) -> Tuple[str, str]:
        self.thinking_time = time() + thinking_time
        
        randomMove = (random.randint(0, state.board.col), random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])) #minimax algorithm
        best_movement = randomMove

        if n_player == 0:
            bestVal = float('-inf')
            shapes = [ShapeConstant.CIRCLE, ShapeConstant.CROSS]

        else:
            bestVal = float('inf')
            shapes = [ShapeConstant.CROSS, ShapeConstant.CIRCLE]
            
        for shape in shapes:
            for i in range(state.board.col):
                stateCopy = copy.deepcopy(state)
                if place(stateCopy, 0, shape, i) == -1:
                    continue
                currMove = (i,shape)
                value = self.miniMaxVal(stateCopy, 2, float('-inf'), float('inf'), (n_player + 1) % 2)
                check = (value > bestVal) if (n_player == 0) else (value < bestVal)
                if check:
                    bestVal = value
                    best_movement = currMove

        return best_movement


    def miniMaxVal(self, state: State, depth: int, alpha, beta, player: int):
        winner = is_win(state.board)
        if depth == 0 or winner or time() > (self.thinking_time - 0.01):
            if winner:
                for i, player in enumerate(state.players):
                    if winner[0] == player.shape and winner[1] == player.color:
                        if i == 0:
                            value = 100
                        if i == 1:
                            value = -100
                        break
            else:
                value = self.point_katsu(state.board)
            return value


        if player == 0:
            bestVal = float('-inf')
            shapes = [ShapeConstant.CIRCLE, ShapeConstant.CROSS]
            for shape in shapes:
                # if time() > self.thinking_time:
                #     break
                for i in range(state.board.col):
                    # if time() > self.thinking_time:
                    #     break
                    stateCopy = copy.deepcopy(state)
                    if place(stateCopy, 0, shape, i) == -1:
                        continue
                    value = self.miniMaxVal(stateCopy, depth-1, alpha, beta, 1)
                    bestVal = max( bestVal, value)
                    alpha = max( alpha, value)
                    if beta<= alpha :
                        break

            return bestVal

        else :
            bestVal = float('inf')
            shapes = [ShapeConstant.CROSS, ShapeConstant.CIRCLE]
            for shape in shapes:
                # if time() > self.thinking_time:
                #     break
                for i in range(state.board.col):
                    # if time() > self.thinking_time:
                    #     break
                    stateCopy = copy.deepcopy(state)
                    if place(stateCopy, 1, shape, i) == -1:
                        continue
                    value = self.miniMaxVal(stateCopy, depth-1, alpha, beta, 0)
                    bestVal = min(bestVal, value)
                    beta = min(beta, value)
                    if beta <= alpha :
                        break

            return bestVal

    def point_katsu(self, board: Board) -> int:
        val = 0
        for row in range(board.row):
            for col in range(board.col):
                piece = board[row, col]
                if piece.shape == ShapeConstant.BLANK:
                    break

                streak_way = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                
                for prior in GameConstant.WIN_PRIOR:
                    mark = 0
                    for row_ax, col_ax in streak_way:
                        row_ = row + row_ax
                        col_ = col + col_ax
                        for _ in range(GameConstant.N_COMPONENT_STREAK - 1):
                            if is_out(board, row_, col_):
                                val = max(mark, val)
                                break

                            shape_condition = (
                                prior == GameConstant.SHAPE
                                and piece.shape != board[row_, col_].shape
                            )
                            color_condition = (
                                prior == GameConstant.COLOR
                                and piece.color != board[row_, col_].color
                            )
                            if shape_condition or color_condition:
                                val = max(mark,val)
                                break

                            row_ += row_ax
                            col_ += col_ax
                            mark += 1

                        val = max(val, mark)
        return val 