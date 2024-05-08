from tkinter import *
import tkinter.messagebox

# Constants
PLAYER_X = "X"
PLAYER_O = "O"

# Initialize Tkinter
tk = Tk()
tk.title("Tic Tac Toe")

# Player names input fields
player1_name = Entry(tk, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

# Game state variables
current_player = PLAYER_X
moves = 0
game_over = False

def disable_buttons():
    for button in [button1, button2, button3, button4, button5, button6, button7, button8, button9]:
        button.configure(state=DISABLED)

def check_for_win():
    # Define winning conditions
    winning_conditions = [
        [button1, button2, button3], [button4, button5, button6], [button7, button8, button9],  # Rows
        [button1, button4, button7], [button2, button5, button8], [button3, button6, button9],  # Columns
        [button1, button5, button9], [button3, button5, button7]  # Diagonals
    ]
    
    # Check if any winning condition is met
    for condition in winning_conditions:
        symbols = [button["text"] for button in condition]
        if symbols.count(PLAYER_X) == 3 or symbols.count(PLAYER_O) == 3:
            disable_buttons()
            winner = player1_name.get() if current_player == PLAYER_X else player2_name.get()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", f"{winner} Wins!")
            return True
    
    # Check for a tie
    if moves == 9:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's a Tie!")
        return True
    
    return False

def btn_click(button):
    global current_player, moves, game_over
    if not game_over and button["text"] == " ":
        button["text"] = current_player
        moves += 1
        game_over = check_for_win()
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

def get_move():
    global game_over
    row = col = -1
    while row not in [0, 1, 2, 3] or col not in [0, 1, 2, 3]:
        row = int(input("Enter row (0, 1, or 2) or enter 3 to quit: "))
        if row == 3:
            tk.destroy()
            return
        col = int(input("Enter column (0, 1, or 2) or enter 3 to quit: "))
        if col == 3:
            tk.destroy()
            return
    if buttons[row * 3 + col]["text"] == " ":
        buttons[row * 3 + col].invoke()

# Create buttons
buttons = []
for row in range(3):
    for col in range(3):
        button = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8)
        button.grid(row=row + 3, column=col)
        button.config(command=lambda btn=button: btn_click(btn))
        buttons.append(button)

# Start game loop
while True:
    get_move()
    if game_over:
        break
