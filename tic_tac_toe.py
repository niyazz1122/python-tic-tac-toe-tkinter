
import tkinter as tk
from tkinter import messagebox

# Game window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)

# Game state
current_player = "X"
board = [""] * 9
buttons = []


def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] != "":
            return board[a]

    return None


def make_move(index):
    global current_player

    # Ignore occupied cells
    if board[index] != "":
        return

    board[index] = current_player
    buttons[index].config(
        text=current_player,
        state="disabled"
    )

    winner = check_winner()

    if winner:
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
        disable_board()
        status.config(text=f"Player {winner} wins!")
    elif "" not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        status.config(text="It's a draw!")
    else:
        current_player = "O" if current_player == "X" else "X"
        status.config(text=f"Player {current_player}'s turn")


def disable_board():
    for button in buttons:
        button.config(state="disabled")


def reset_game():
    global current_player

    current_player = "X"
    board[:] = [""] * 9

    for button in buttons:
        button.config(text="", state="normal")

    status.config(text="Player X's turn")


# Heading
status = tk.Label(
    root,
    text="Player X's turn",
    font=("Arial", 16)
)
status.grid(row=0, column=0, columnspan=3, pady=10)

# Create 9 game buttons
for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 24, "bold"),
        width=5,
        height=2,
        command=lambda index=i: make_move(index)
    )
    button.grid(
        row=(i // 3) + 1,
        column=i % 3,
        padx=4,
        pady=4
    )
    buttons.append(button)

# Restart button
restart = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 12),
    command=reset_game
)
restart.grid(row=4, column=0, columnspan=3, pady=12)

root.mainloop()
