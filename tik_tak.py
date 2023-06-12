import tkinter.messagebox
from tkinter import *

# Create a Tkinter window
root = Tk()
root.title("Tic Tac Toe")

# Variable to track the current player
current_player = "X"

# Create a list to represent the Tic Tac Toe board
board = [" " for _ in range(9)]

# Function to handle a button click event
def button_click(index):
    global current_player

    # Check if the clicked button is already marked
    if board[index] == " ":
        # Mark the button with the current player's symbol (X or O)
        board[index] = current_player
        buttons[index].config(text=current_player, bg="black", fg="white", font=("Arial", 24, "bold"))

        # Check if the current player wins
        if check_win(current_player):
            tkinter.messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            reset_game()
        # Check if the game is a draw
        elif check_draw():
            tkinter.messagebox.showinfo("Tic Tac Toe", "The game is a draw!")
            reset_game()
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"

# Function to check if a player wins
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True

    return False

# Function to check if the game is a draw
def check_draw():
    return " " not in board

# Function to reset the game
def reset_game():
    global current_player, board

    # Clear the board
    board = [" " for _ in range(9)]

    # Clear the button text and reset colors
    for button in buttons:
        button.config(text=" ", bg="black", fg="white", font=("Arial", 24, "bold"))

    # Reset the current player
    current_player = "X"

# Create buttons for the Tic Tac Toe board
buttons = []
for i in range(9):
    button = Button(root, text=" ", width=10, height=5,
                    command=lambda index=i: button_click(index), bg="black", fg="white", font=("Arial", 24, "bold"))
    buttons.append(button)
    button.grid(row=i // 3, column=i % 3)

# Start the Tkinter event loop
root.mainloop()
