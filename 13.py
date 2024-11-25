# Tic-Tac-Toe with Minimax Algorithm

# Define the board size and the player symbols
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Check if the current board state is a winning condition for a player
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Check if the board is full (tie condition)
def is_full(board):
    return all(board[i][j] != EMPTY for i in range(3) for j in range(3))

# Minimax algorithm to find the best move for the current player
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, PLAYER_X):
        return 1
    if check_winner(board, PLAYER_O):
        return -1
    if is_full(board):
        return 0
    
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Find the best move for the current player using minimax
def best_move(board):
    best_val = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_val = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

# Main function to play the game
def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    player_turn = PLAYER_X
    
    while True:
        print_board(board)
        
        if player_turn == PLAYER_X:
            print("Player X's turn (AI):")
            move = best_move(board)
            board[move[0]][move[1]] = PLAYER_X
        else:
            print("Player O's turn (Human):")
            try:
                row, col = map(int, input("Enter row and column (0, 1, 2) separated by a space: ").split())
                if board[row][col] != EMPTY:
                    print("Cell already occupied, try again.")
                    continue
                board[row][col] = PLAYER_O
            except (ValueError, IndexError):
                print("Invalid move. Please try again.")
                continue
        
        # Check for a winner or tie
        if check_winner(board, PLAYER_X):
            print_board(board)
            print("Player X (AI) wins!")
            break
        if check_winner(board, PLAYER_O):
            print_board(board)
            print("Player O wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch turns
        player_turn = PLAYER_O if player_turn == PLAYER_X else PLAYER_X

# Run the game
if __name__ == "__main__":
    play_game()
