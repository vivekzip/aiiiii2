def find_best_move(board):
  """
  Finds the best move for a given game board.
  Args:
    board: A 2D list representing the game board.
  Returns:
    A tuple containing the row and column of the best move.
  """
  best_move = (0, 0)
  best_value = 0
  for row in range(len(board)):
    for col in range(len(board[0])):
      if board[row][col] > best_value:
        best_move = (row, col)
        best_value = board[row][col]
  return best_move

# Example usage:
board = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]

best_move = find_best_move(board)
print("The Optimal Move is :")
print(f"ROW: {best_move[0]} COL: {best_move[1]}")