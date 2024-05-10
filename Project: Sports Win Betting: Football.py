import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

class FootballMatch:
    def __init__(self):
        self.winner = None

    def simulate_match(self, match_name):
        # Adjust the weights to increase winning chances for higher scores
        score1 = random.choices(range(6), weights=[15, 20, 25, 20, 15, 5])[0]
        score2 = random.choices(range(6), weights=[15, 20, 25, 20, 15, 5])[0]
        
        if score1 > score2:
            self.winner = match_name.split(" vs. ")[0]
        elif score2 > score1:
            self.winner = match_name.split(" vs. ")[1]
        else:
            self.winner = "Draw"

        return score1, score2, self.winner  # Also return the winner

class BetWindow:
    def __init__(self, match_name, menu_window, football_match):
        self.match_name = match_name
        self.menu_window = menu_window  # Store the MenuWindow instance
        self.football_match = football_match  # Store the FootballMatch instance
        self.bet_window = tk.Tk()
        self.bet_window.title("Place Bet")

        team_label = tk.Label(self.bet_window, text=f"Choose a team to bet on ({match_name}):")
        team_label.pack()

        self.team_choice = tk.StringVar()
        team_choice_radio = tk.Radiobutton(self.bet_window, text=match_name.split(" vs. ")[0], variable=self.team_choice, value=match_name.split(" vs. ")[0])
        team_choice_radio.pack()
        team_choice_radio = tk.Radiobutton(self.bet_window, text=match_name.split(" vs. ")[1], variable=self.team_choice, value=match_name.split(" vs. ")[1])
        team_choice_radio.pack()

        amount_label = tk.Label(self.bet_window, text="Enter bet amount:")
        amount_label.pack()
        self.amount_entry = tk.Entry(self.bet_window)
        self.amount_entry.pack()

        bet_button = tk.Button(self.bet_window, text="Place Bet", command=lambda: self.place_bet())
        bet_button.pack()

    def place_bet(self):
        team_name = self.team_choice.get()
        amount = float(self.amount_entry.get())

        # Simulate match to determine winner
        _, _, winner = self.football_match.simulate_match(self.match_name)

        if winner == "Draw":
            messagebox.showinfo("Draw", f"The match ended in a draw.\nNo winners or losers.")
        elif team_name == winner:
            payout = amount * 2
            self.menu_window.update_balance(payout)  # Update balance with winning amount
            messagebox.showinfo("Congratulations!", f"You won {payout} units.\nMatch Winner: {winner}")
        else:
            self.menu_window.update_balance(-amount)  # Deduct bet amount from balance
            messagebox.showinfo("Sorry!", f"You lost your bet.\nMatch Winner: {winner}")

        self.bet_window.geometry("300x150")  # Adjust size 
        self.bet_window.destroy()

class MenuWindow:
    def __init__(self, player_name):
        self.player_name = player_name
        self.menu_window = tk.Tk()
        self.menu_window.title("Main Menu")
        self.menu_window.geometry("600x400")
        self.match_names = [
            "Germany vs. France",
            "Brazil vs. Argentina",
            "England vs. Germany",
            "France vs. Portugal",
            "Korea vs. Japan",
            "Costa Rica vs. Mexico",
            "Australia vs. Netherlands"
            
        ]
        self.current_match_index = 0  # Initialize current match index

        self.tab_control = ttk.Notebook(self.menu_window)

        self.game_tab = tk.Frame(self.tab_control)
        self.tab_control.add(self.game_tab, text="Game")
        self.tab_control.pack(expand=1, fill="both")

        menu_label = tk.Label(self.game_tab, text=f"Welcome, {self.player_name}!", font=("Arial", 14, "bold"))
        menu_label.pack(pady=20)

        self.match_label = tk.Label(self.game_tab, text="Scheduled Match of the Day:")
        self.match_label.pack()

        self.match_info_label = tk.Label(self.game_tab, text="Italy vs. Spain")
        self.match_info_label.pack()

        start_game_button = tk.Button(self.game_tab, text="Place Bet", command=self.start_game)
        start_game_button.pack(pady=10)

        play_again_button = tk.Button(self.game_tab, text="Play Again", command=self.play_again)
        play_again_button.pack(pady=10)

        quit_game_button = tk.Button(self.game_tab, text="Quit Game", command=self.quit_game)
        quit_game_button.pack(pady=10)
        
        # Initialize bankroll
        self.bankroll = 1000  # Starting balance

        # Display initial balance
        self.balance_label = tk.Label(self.game_tab, text=f"Bankroll: {self.bankroll} units")
        self.balance_label.pack()

        # Create FootballMatch instance
        self.football_match = FootballMatch()

    def update_balance(self, amount):
        self.bankroll += amount
        self.balance_label.config(text=f"Bankroll: {self.bankroll} units")

    def start_game(self):
        match_name = self.match_info_label.cget("text")
        BetWindow(match_name, self, self.football_match)  # Pass FootballMatch instance

    def play_again(self):
        new_match_name = self.match_names[self.current_match_index]
        self.current_match_index = (self.current_match_index + 1) % len(self.match_names)
        self.match_info_label.config(text=new_match_name)
        BetWindow(new_match_name, self, self.football_match)  # Pass FootballMatch instance

    def quit_game(self):
        self.menu_window.destroy()

class PlayerInfoWindow:
    def get_player_info_window(self):
        self.player_info_window = tk.Tk()
        self.player_info_window.title("Player Information")

        welcome_label = tk.Label(self.player_info_window, text="Welcome to Sports Win Betting Football", font=("Arial", 14, "bold"))
        welcome_label.pack(pady=10)

        info_label = tk.Label(self.player_info_window, text="--- Player Information ---", font=("Arial", 12, "bold"))
        info_label.pack(pady=10)

        name_label = tk.Label(self.player_info_window, text="Enter your name:")
        name_label.pack()
        self.name_entry = tk.Entry(self.player_info_window)
        self.name_entry.pack()

        age_label = tk.Label(self.player_info_window, text="Enter your age:")
        age_label.pack()
        self.age_entry = tk.Entry(self.player_info_window)
        self.age_entry.pack()

        submit_button = tk.Button(self.player_info_window, text="Submit", command=self.submit_info)
        submit_button.pack(pady=20)

    def submit_info(self):
        player_name = self.name_entry.get()
        player_age = int(self.age_entry.get())

        if player_age < 21:
            messagebox.showerror("Error", "You must be at least 21 years old to play this game.")
            self.player_info_window.destroy()  # Close the current window
            self.get_player_info_window()  # Reopen the player info window
        else:
            self.player_info_window.destroy()
            MenuWindow(player_name)

class GameWindow:
    def __init__(self):
        self.intro_window = None
        self.player_info_window = PlayerInfoWindow()

    def game_introduction(self):
        self.intro_window = tk.Tk()
        self.intro_window.title("Sports Win Betting Football!")

        intro_label = tk.Label(self.intro_window, text="--- Sports Win Betting Football! ---", font=("Arial", 16, "bold"))
        intro_label.pack(pady=20)

        welcome_label = tk.Label(self.intro_window, text="Welcome to Sports Win Betting Football! You will be betting on a football match between two teams.", wraplength=400)
        welcome_label.pack(pady=10)

        reminder_label = tk.Label(self.intro_window, text="*Reminder: This game is only played for ages 21 years old and above.", font=("Arial", 10, "italic"))
        reminder_label.pack(pady=10)

        def next_step():
            self.intro_window.destroy()
            self.player_info_window.get_player_info_window()

        next_button = tk.Button(self.intro_window, text="Start Betting", command=next_step)
        next_button.pack(pady=20)

        self.intro_window.mainloop()

if __name__ == "__main__":
    game = GameWindow()
    game.game_introduction()

if __name__ == "__main__":
    game = GameWindow()
    game.game_introduction()

