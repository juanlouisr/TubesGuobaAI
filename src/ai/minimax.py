import random
import copy

from time import time

from src.constant import GameConstant, ShapeConstant
from src.model import State, Board

from typing import Tuple, List

from src.utility import is_win,katsu_pointo,place


class Minimax:
    def __init__(self):
        pass

    def find(self, state: State, n_player: int, thinking_time: float) -> Tuple[str, str]:
        self.thinking_time = time() + thinking_time
        
        stateCopy = copy.deepcopy(state)
        moves = []
        self.miniMaxVal(stateCopy, 3, float('-inf'), float('inf'), n_player, moves)

        randomMove = (random.randint(0, state.board.col), random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])) #minimax algorithm
        best_movement = moves[0] if len(moves) != 0 else randomMove
        return best_movement


    def miniMaxVal(self, state: State, depth: int, alpha, beta, player: int, moves: list):
        if depth == 0 or is_win(state.board):
            return katsu_pointo(state.board)
        # place(state: State, n_player: int, shape: str, col: str) -> int:

        if player == 0:
            bestVal = float('-inf')
            shapes = [ShapeConstant.CIRCLE, ShapeConstant.CROSS]
            for shape in shapes:
                for i in range(state.board.col):
                    stateCopy = copy.deepcopy(state)
                    if place(stateCopy, 0, shape, i) == -1:
                        continue
                    currMove = (i,shape)
                    moves.append(currMove)
                    value = self.miniMaxVal(stateCopy, depth-1, alpha, beta, 1, moves)
                    bestVal = max( bestVal, value)
                    alpha = max( alpha, value)
                    if beta<= alpha :
                        break
            return bestVal

        else :
            bestVal = float('inf')
            shapes = [ShapeConstant.CROSS, ShapeConstant.CIRCLE]
            for shape in shapes:
                for i in range(state.board.col):
                    stateCopy = copy.deepcopy(state)
                    if place(stateCopy, 1, shape, i) == -1:
                        continue
                    currMove = (i,shape)
                    moves.append(currMove)
                    value = self.miniMaxVal(stateCopy, depth-1, alpha, beta, 0, moves)
                    bestVal = min(bestVal, value)
                    beta = min(beta, value)
                    if beta <= alpha :
                        break
            return bestVal
    # function minimax(state, depth, alpha, beta, isMaximizingPlayer):
    # if current board state is a terminal state :
    #     return value of the board
    
    # if player == 0 :
    #     bestVal = -INFINITY
    #     for each move in board :
    #         value = minimax(move, depth-1, alpha, beta, 1)
    #         bestVal = max( bestVal, value) 
    #         alpha = max( alpha, value)
    #         if beta<= alpha :
    #             break 
    #     return bestVal

    # else :
    #     bestVal = +INFINITY 
    #     for each move in board :
    #         value = minimax(move, depth-1, alpha, beta, 0)
    #         bestVal = min( bestVal, value) 
    #         beta = min( beta, value)
    #         if beta<= alpha :
    #             break
    #     return bestVal

