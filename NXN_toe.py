import tkinter as tk
import random

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    n = len(board)
    for i in range(n):
        if all(board[i][j] == player for j in range(n)) or all(board[j][i] == player for j in range(n)):
            return True
    if all(board[i][i] == player for i in range(n)) or all(board[i][n-1-i] == player for i in range(n)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != "" for i in range(len(board)) for j in range(len(board)))

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

def switch_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    status_label.config(text=f"Player {current_player}'s turn")

def start_game():
    global n, board, current_player, game_over

    n = int(entry.get())
    board = [["" for _ in range(n)] for _ in range(n)]
    current_player = "X"
    game_over = False

    for widget in root.winfo_children():
        widget.destroy()

    for row in range(n):
        for col in range(n):
            buttons[row][col] = tk.Button(root, text="", font=("Helvetica", 20), width=5, height=2,
                                          command=lambda row=row, col=col: on_button_click(row, col))
            buttons[row][col].grid(row=row, column=col)

    status_label = tk.Label(root, text="Player X's turn", font=("Helvetica", 14))
    status_label.grid(row=n, column=0, columnspan=n)

    restart_button = tk.Button(root, text="Restart", font=("Helvetica", 12), command=start_game)
    restart_button.grid(row=n+1, column=0, columnspan=n)

# Initialize the GUI
root = tk.Tk()
root.title("Tic Tac Toe")

n = 3  # Default size

buttons = [[None for _ in range(n)] for _ in range(n)]
board = [["" for _ in range(n)] for _ in range(n)]
current_player = "X"
game_over = False

entry_label = tk.Label(root, text="Enter the size of the board:")
entry_label.grid(row=0, column=0, columnspan=n)
entry = tk.Entry(root)
entry.grid(row=1, column=0, columnspan=n)

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.grid(row=2, column=0, columnspan=n)

root.mainloop()
