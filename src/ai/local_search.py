import random
import copy
from time import time

from src.constant import ShapeConstant
from src.model import State
from src.utility import is_out, is_win, is_full, place

from typing import Tuple, List


class LocalSearch:
	def __init__(self):
		pass

	def find(self, state: State, n_player: int, thinking_time: float) -> Tuple[str, str]:
		self.thinking_time = time() + thinking_time
		random_movement = (random.randint(0, state.board.col), random.choice([ShapeConstant.CROSS, ShapeConstant.CIRCLE]))
		best_movement = random_movement
		
		x = hillclimbing(state, n_player)
		y = state.players[n_player].shape

		choosed_move = [x, y]
		best_movement = choosed_move
		
		return best_movement

	def hillclimbing(state: State):
		current_value = 0
		neighbor_value = 0
		choosed_col = 0
		
		for col in range(state.board.col) :
			for row in range(state.board.row - 1, -1, -1):
					if state.board[row, col].shape == ShapeConstant.BLANK:
						stateCopy = copy.deepcopy(state)
						place(stateCopy, n_player, statecopy.players[n_player].shape, col)
						neighbor_value = check_value(stateCopy.board, row, col)
						break
						
			if neighbor_value >= current_value:
				current_value = neighbor_value
				choosed_col = col
		return col
	
	def check_value(board: Board, row: int, col: int):
		piece = board[row, col]
		if piece.shape == ShapeConstant.BLANK:
			return None

		streak_way = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
		current_value = 0
		
		for prior in GameConstant.WIN_PRIOR:
			for row_ax, col_ax in streak_way:
				value = 0
				row_ = row + row_ax
				col_ = col + col_ax
				for _ in range(GameConstant.N_COMPONENT_STREAK - 1):
					if is_out(board, row_, col_):
						if current_value < value :
							current_value = value
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
						if current_value < value :
							current_value = value
						break
						
					row_ += row_ax
					col_ += col_ax
					value += 1
					
				row_ = row - row_ax
				col_ = col - col_ax
				
				for _ in range(GameConstant.N_COMPONENT_STREAK - 1):
					if is_out(board, row_, col_):
						if current_value < value :
							current_value = value
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
						if current_value < value :
							current_value = value
						break
						
					if value = 3:
						break
						
					row_ -= row_ax
					col_ -= col_ax
					value += 1
		
		return current_value
