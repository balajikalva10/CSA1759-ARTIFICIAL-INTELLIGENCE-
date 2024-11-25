# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Check if placing a queen at (row, col) is safe
def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == "Q": return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q": return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == "Q": return False
    return True

# Solve N-Queens problem
def solve_nqueens(board, col, n):
    if col >= n: return True  # All queens are placed
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"
            if solve_nqueens(board, col + 1, n): return True
            board[row][col] = "."  # Backtrack
    return False

# Input and solve
N = 8
board = [["."] * N for _ in range(N)]
if solve_nqueens(board, 0, N):
    print("Solution:")
    print_board(board)
else:
    print("No solution exists.")

