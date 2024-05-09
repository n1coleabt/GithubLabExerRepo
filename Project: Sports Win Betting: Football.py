import random

class FootballMatch:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.score1 = random.randint(0, 5)
        self.score2 = random.randint(0, 5)
        self.winner = None  # Add winner attribute

class SportsWinBetting:
    def __init__(self):
        self.teams = {}
        self.bets = []

    def add_team(self, team_name):
        self.teams[team_name] = {'wins': 0, 'losses': 0}

    def place_bet(self, team_name, amount):
        self.bets.append({'team': team_name, 'amount': amount})

    def resolve_game(self, winning_team):
        for bet in self.bets:
            if bet['team'] == winning_team:
                payout = bet['amount'] * 2
                print(f"Congratulations! You won {payout} units.")
            else:
                print("Sorry, you lost your bet.")
        self.bets = []
    
class BettingSimulation:
    def __init__(self):
        self.bankroll = 0
        self.betting_system = SportsWinBetting()
        self.matches = []
        self.match_history = []
        self.upcoming_matches = [("Manchester", "Spain"), ("Brazil", "Korea")]

    def simulate_match(self, team1, team2):
        if len(team1) == 0 or len(team2) == 0:
            print("Invalid team names.")
            return None
        match = FootballMatch(team1, team2)
        self.matches.append(match)
        return match

    def calculate_odds(self, match):
        if match is None:
            return None
        total_goals = match.score1 + match.score2
        odds_decimal = 10.0 / total_goals
        return odds_decimal

    def place_bet(self, match, team_name, amount):
        if match is None:
            print("Invalid match.")
            return 0, False
        odds = self.calculate_odds(match)
        if odds is None:
            print("Unable to calculate odds.")
            return 0, False
        if amount <= 0:
            print("Invalid bet amount.")
            return 0, False
        if amount > self.bankroll:
            print("Insufficient funds.")
            return 0, False
        self.betting_system.place_bet(team_name, amount)
        self.bankroll -= amount
        return odds, True

    def display_previous_games(self):
        print("\nPrevious Game Results:")
        for game in self.match_history:
            print(f"{game['team1']} {game['score1']} - {game['score2']} {game['team2']}")
    
    def display_upcoming_matches(self):
        print("\nUpcoming Matches:")
        for idx, (team1, team2) in enumerate(self.upcoming_matches, start=1):
            print(f"{idx}. {team1} vs {team2}")
   
    def predict_game(self, team1, team2):
        return random.choice([team1, team2])

    def simulate_match(self, team1, team2):
        if len(team1) == 0 or len(team2) == 0:
            print("Invalid team names.")
            return None
        
        predicted_winner = self.predict_game(team1, team2)
        
        match = FootballMatch(team1, team2)
        match.winner = predicted_winner
        self.matches.append(match)
        return match

def get_player_info():
    print("Welcome to Sports Win Betting Football")
    print("\n--- Player Information ---")
    player_name = input("Enter your name: ")
    player_age = int(input("Enter your age: "))
    return player_name, player_age

def display_menu():
    print("\nMenu:")
    print("1. Start Game")
    print("2. Quit the Game")
    print("3. Play Again")

def game_introduction():
    print("\n--- Sports Win Betting Football! ---")
    print("Welcome to Sports Win Betting Football! You will be betting on a football match between two teams.") 
    print("\n*Reminder: This game is only played for ages 21 years old and above.")   

def main():
    game_introduction()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            pass
            player_name, player_age = get_player_info()
            while player_age < 21:
                print("Sorry, you must be 21 years or older to play.")
                player_name, player_age = get_player_info()
                
            # Example match schedule for the day
            print("\nAvailable Matches Today:")
            print("1. Real Madrid vs Barcelona")
            match_choice = input("Choose a match (enter the number): ")

            if match_choice == '1':
                team1 = "Real Madrid"
                team2 = "Barcelona"
            else:
                print("Invalid match choice.")
                continue
            
            while True:
                # Ready to play
                print("\nReady to place bet?")
                print("1. Yes")
                print("2. No")
                match_choice = input("Choose an option (enter the number): ")
            
                if match_choice == '1':
                    option = "Yes"
                    break
                elif match_choice == '2':
                    option = "No"
                else:
                    print("Invalid option.")
                    continue
                       
            sim = BettingSimulation()
            sim.bankroll = float(input("Enter your starting balance: $"))
            sim.betting_system.add_team(team1)
            sim.betting_system.add_team(team2)

            print(f"\nTeams competing: {team1} vs {team2}")

            match1 = sim.simulate_match(team1, team2)
            if match1:
                amount_bet = float(input(f"\nHello {player_name}, enter your bet amount: $"))
                if amount_bet <= sim.bankroll:
                    odds, outcome = sim.place_bet(match1, team1, amount_bet)

                    if outcome:
                        print(f"\nBankroll: ${sim.bankroll}")
                        print(f"Match - {match1.team1} vs {match1.team2}:")
                        print(f"Final Score: {match1.score1} - {match1.score2}")
                        print(f"Bet Amount: ${amount_bet}")
                        print(f"Odds: {odds:.2f}")
                        print(f"Bet Outcome: {'Win' if outcome else 'Loss'}")
                    else:
                        print("Error placing bet.")
                else:
                    print("Insufficient funds.")

                sim.match_history.append({'team1': match1.team1, 'team2': match1.team2, 
                                          'score1': match1.score1, 'score2': match1.score2})

                play_again_input = input("\nDo you want to play again? (yes/no): ")
                if play_again_input.lower() != 'yes':
                    print("\nThank you for playing Sports Win Betting Football!.")
                    break
                elif play_again_input.lower() == 'no':
                    break  # Exit the betting loop
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            sim.display_previous_games()
            
            sim.display_upcoming_matches()
            match_choice = input("Choose an upcoming match to bet (enter the number): ")

            try:
                match_idx = int(match_choice) - 1
                if match_idx < 0 or match_idx >= len(sim.upcoming_matches):
                    print("Invalid match choice.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            sim.betting_system.add_team(team1)
            sim.betting_system.add_team(team2)

            print(f"\nYou are placing a bet on the match {team1} vs {team2} scheduled for {match_choice}")
            while True:
                try:
                    amount_bet = float(input(f"\nHello {player_name}, enter your bet amount: $"))
                    if amount_bet > sim.bankroll:
                        print("Insufficient funds.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Bet amount must be a number.")

            match1 = sim.simulate_match(team1, team2)
            if match1:
                odds, outcome = sim.place_bet(match1, team1, amount_bet)

                if outcome:
                    print(f"\nBankroll: ${sim.bankroll}")
                    print(f"Match - {team1} vs {team2}:")
                    print(f"Match Date: {match_choice}")
                    print(f"Bet Amount: ${amount_bet}")
                    print(f"Odds: {odds:.2f}")
                    print("Bet placed successfully!")
                    print(f"Predicted winner: {match1.winner}")
                else:
                    print("Error placing bet.")
                    
        elif choice == '2':
            print("Thank you for playing Sports Win Betting Football!")
            break
        elif choice == '3':
            print("Play again")
            play_again = input("Do you want to start the game again? (yes/no): ")
            if play_again.lower() == 'yes':
                continue  # Restart the game loop
            else:
                print("Thank you for playing Sports Win Betting Football!")
                break
        else:
            print("Invalid choice. Please try again.")
                   
if __name__ == "__main__":
    main()
