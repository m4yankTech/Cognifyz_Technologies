import random

def print_board(board):
    """Prints the Tic Tac Toe board."""
    print("Tic Tac Toe")
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

def check_winner(board, player):
    """Checks if a player has won the game."""
    for i in range(3):
        if all(cell == player for cell in board[i]):  # Check rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Check columns
            return True
    if all(board[i][i] == player for i in range(3)):  # Check diagonal
        return True
    if all(board[i][2-i] == player for i in range(3)):  # Check other diagonal
        return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        if ' ' in row:
            return False
    return True

def get_player_move(board):
    """Gets a valid move from the player."""
    while True:
        try:
            row, col = map(int, input("Enter your move (row col): ").split())
            if board[row - 1][col - 1] != ' ':
                print("That position is already taken!")
            elif row not in range(1, 4) or col not in range(1, 4):
                print("Invalid row or column! Please enter values between 1 and 3.")
            else:
                return row - 1, col - 1
        except ValueError:
            print("Invalid input! Please enter two integers separated by a space.")

def get_computer_move(board):
    """Gets a valid move from the computer."""
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)

def play_game():
    """Main function to play the game."""
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    random.shuffle(players)
    current_player = players[0]

    while True:
        print_board(board)

        if current_player == 'X':
            print("\nYour turn (X)")
            row, col = get_player_move(board)
        else:
            print("\nComputer's turn (O)")
            input("Press Enter to see computer's move...")
            row, col = get_computer_move(board)
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"\nPlayer {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("\nIt's a tie!")
            break

        current_player = 'X' if current_player == 'O' else 'O'

play_game()

