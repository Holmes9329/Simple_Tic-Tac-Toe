def print_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def get_input(player, board):
    while True:
        choice = input(f"{player}'s turn. Please select a position from 1-9: ")
        if not choice.isdigit():
            print("Invalid input! Please enter a number from 1-9.")
            continue
        choice = int(choice) - 1
        if choice < 0 or choice > 8:
            print("Invalid input! Please enter a number from 1-9.")
            continue
        if board[choice] != " ":
            print("That position is already taken! Please select another position.")
            continue
        return choice

def check_win(board):
    win_positions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != " ":
            return board[pos[0]]
    if " " not in board:
        return "Tie"
    return None

def play_game():
    board = [" "] * 9
    print_board([str(i+1) for i in range(9)])
    player = "X"
    while True:
        choice = get_input(player, board)
        board[choice] = player
        print_board(board)
        winner = check_win(board)
        if winner is not None:
            if winner == "Tie":
                print("The game is a tie!")
            else:
                print(f"{winner} has won the game!")
            return
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    play_game()
