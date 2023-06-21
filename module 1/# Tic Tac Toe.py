# Tic Tac Toe

# Create the game board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

# Function to check if any player has won
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to check if the board is full
def check_draw():
    return ' ' not in board

# Function to make a move
def make_move(player, position):
    if board[position] == ' ':
        board[position] = player
        return True
    return False

# Function to play the game
def play_game():
    current_player = 'X'
    while True:
        display_board()
        print("Player", current_player)
        position = int(input("Enter a position (0-8): "))
        if position < 0 or position > 8:
            print("Invalid position. Try again.")
            continue
        if make_move(current_player, position):
            if check_win(current_player):
                display_board()
                print("Player", current_player, "wins!")
                break
            elif check_draw():
                display_board()
                print("It's a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Position already occupied. Try again.")

# Start the game
play_game()
