#  tic tac toe game - done

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*9)

def check_winner(board,player_turn):
    for i in range(3):
        if all(board[i][j] == player_turn for j in range(3)) or all(board[j][i] == player_turn for j in range(3)):
            return True
    if (board[0][0] == player_turn and board[1][1] == player_turn and board[2][2] == player_turn ):
        return True
    if (board[0][2] == player_turn and board[1][1] == player_turn and board[2][0] == player_turn ):
        return True
    
    return False

def is_tie(board,player_turn): 
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def play_game():
    board = [[" "]*3 for _ in range(3)]
    player_turn = "X"

    while True:
        print_board(board)
        print(f"Player {player_turn}'s turn:")

        try:
            row,col = map(int, input("Enter row and col (0,1,2): ").split())
            if(board[row][col] !=" "):
                print("Cell already taken - try again")
                continue
        except(ValueError,IndexError):
            print("Invalid input! try again")
            continue

        board[row][col] = player_turn

        if check_winner(board,player_turn):
            print_board(board)
            print(f"Player {player_turn} Won !!")
            break

        if is_tie(board,player_turn):
            print_board(board)
            print("The game is TIE")
            break

        player_turn = "O" if player_turn == "X" else "X"

if __name__ == "__main__":
    play_game()

















# below code is chatgpt code - see for reference


# def print_board(board):
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 5)

# def check_winner(board, player):
#     for i in range(3):
#         if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
#             return True
#     if board[0][0] == player and board[1][1] == player and board[2][2] == player:
#         return True
#     if board[0][2] == player and board[1][1] == player and board[2][0] == player:
#         return True
#     return False

# def is_full(board):
#     return all(board[i][j] != " " for i in range(3) for j in range(3))

# def play_game():
#     board = [[" "] * 3 for _ in range(3)]
#     player_turn = "X"
    
#     while True:
#         print_board(board)
#         print(f"Player {player_turn}'s turn:")
        
#         try:
#             row, col = map(int, input("Enter row and column (0, 1, 2): ").split())
#             if board[row][col] != " ":
#                 print("Cell already taken. Try again.")
#                 continue
#         except (ValueError, IndexError):
#             print("Invalid input! Enter 0, 1, or 2 for row and column.")
#             continue
        
#         board[row][col] = player_turn
        
#         if check_winner(board, player_turn):
#             print_board(board)
#             print(f"Player {player_turn} wins!")
#             break
        
#         if is_full(board):
#             print_board(board)
#             print("It's a tie!")
#             break
        
#         player_turn = "O" if player_turn == "X" else "X"

# if __name__ == "__main__":
#     play_game()
