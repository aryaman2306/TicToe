import tkinter as tk
import random

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != "" for i in range(3) for j in range(3))

def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]
    return random.choice(empty_cells)

def on_button_click(row, col):
    if board[row][col] == "" and not game_over:
        btn = buttons[row][col]
        btn.config(text=current_player, state=tk.DISABLED)
        board[row][col] = current_player

        if check_win(board, current_player):
            status_label.config(text=f"Player {current_player} wins!")
            game_over = True
        elif is_board_full(board):
            status_label.config(text="It's a draw!")
            game_over = True
        else:
            switch_player()

        if not game_over and current_player == "X":
            row, col = computer_move(board)
            buttons[row][col].invoke()

def switch_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    status_label.config(text=f"Player {current_player}'s turn")

def restart_game():
    global board, current_player, game_over
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", state=tk.NORMAL)

    status_label.config(text="Player X's turn")

# Initialize the GUI
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [[None for _ in range(3)] for _ in range(3)]
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=("Helvetica", 20), width=5, height=2,
                                      command=lambda row=row, col=col: on_button_click(row, col))
        buttons[row][col].grid(row=row, column=col)

status_label = tk.Label(root, text="Player X's turn", font=("Helvetica", 14))
status_label.grid(row=3, column=0, columnspan=3)

restart_button = tk.Button(root, text="Restart", font=("Helvetica", 12), command=restart_game)
restart_button.grid(row=4, column=0, columnspan=3)

root.mainloop()
