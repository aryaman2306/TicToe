import tkinter as tk

def check_win(board, player):
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
    global game_over
    if board[row][col] == "" and not game_over:
        buttons[row][col].config(text=current_player, state=tk.DISABLED)
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
    current_player = "O" if current_player == "X" else "X"
    status_label.config(text=f"Player {current_player}'s turn")

def start_game():
    global n, board, buttons, current_player, game_over, status_label

    try:
        n = int(entry.get())
        if n < 2:
            raise ValueError
    except ValueError:
        status_label.config(text="Please enter a valid board size (>=2).")
        return

    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    board = [["" for _ in range(n)] for _ in range(n)]
    buttons = [[None for _ in range(n)] for _ in range(n)]
    current_player = "X"
    game_over = False

    # Create the board buttons
    for row in range(n):
        for col in range(n):
            btn = tk.Button(root, text="", font=("Helvetica", 20), width=5, height=2,
                            command=lambda r=row, c=col: on_button_click(r, c))
            btn.grid(row=row, column=col)
            buttons[row][col] = btn

    # Status label
    status_label = tk.Label(root, text="Player X's turn", font=("Helvetica", 14))
    status_label.grid(row=n, column=0, columnspan=n)

    # Restart button
    restart_button = tk.Button(root, text="Restart", font=("Helvetica", 12), command=start_game)
    restart_button.grid(row=n+1, column=0, columnspan=n)

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

n = 3  # Default board size
board = []
buttons = []
current_player = "X"
game_over = False

# Entry for board size
entry_label = tk.Label(root, text="Enter board size (>=2):")
entry_label.grid(row=0, column=0, columnspan=3)

entry = tk.Entry(root)
entry.grid(row=1, column=0, columnspan=3)

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.grid(row=2, column=0, columnspan=3)

status_label = tk.Label(root, text="", font=("Helvetica", 14))
status_label.grid(row=3, column=0, columnspan=3)

root.mainloop()

