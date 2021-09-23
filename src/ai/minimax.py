import random
import copy
from time import time

from src.constant import ShapeConstant
from src.model import State, Board

from typing import Tuple, List


class Minimax:
    def __init__(self):
        pass

    def find(self, state: State, n_player: int, thinking_time: float) -> Tuple[str, str]:
        self.thinking_time = time() + thinking_time
        
        boardCopy = copy.deepcopy(state.board)
        

    # function minimax(board, depth, alpha, beta, isMaximizingPlayer):
    # if current board state is a terminal state :
    #     return value of the board
    
    # if isMaximizingPlayer :
    #     bestVal = -INFINITY 
    #     for each move in board :
    #         value = minimax(board, depth+1, false)
    #         bestVal = max( bestVal, value) 
    #         alpha = max( alpha, value)
    #         if beta<= alpha :
    #             break 
    #     return bestVal

    # else :
    #     bestVal = +INFINITY 
    #     for each move in board :
    #         value = minimax(board, depth+1, true)
    #         bestVal = min( bestVal, value) 
    #         beta = max( beta, value)
    #         if beta<= alpha :
    #             break 

    #     return bestVal

        best_movement = (random.randint(0, state.board.col), random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE])) #minimax algorithm

        return best_movement


    def miniMaxVal(self, board: Board, alpha: int, beta: int, isMaximazingPlayer: bool)
