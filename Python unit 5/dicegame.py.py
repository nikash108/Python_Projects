import random 
import time 
 
def roll_dice(): 
    return random.randint(1, 6), random.randint(1, 6) 
 
def print_roll(name, roll): 
    print(f"{name} rolled: {roll[0]} + {roll[1]} = {sum(roll)}") 
 
def play_dice(): 
    scores = { 
        "Player1": 0, 
        "Player2": 0, 
        "Player3": 0, 
        "Player4": 0, 
        "Computer": 0 
    } 
 
    rounds = int(input("Enter number of rounds: ")) 
 
    for i in range(1, rounds + 1): 
        input(f"\n       Press Enter to roll (Round {i})...") 
 
        print("Rolling", end="") 
        for _ in range(3): 
            print(".", end="", flush=True) 
            time.sleep(0.5) 
        print("\n") 
 
        rolls = {} 
 
        # Roll for all players 
        for player in scores: 
            roll = roll_dice() 
            rolls[player] = sum(roll) 
            print_roll(player, roll) 
 
        # Find winner of round 
        max_score = max(rolls.values()) 
        winners = [p for p in rolls if rolls[p] == max_score] 
 
        if len(winners) == 1: 
            winner = winners[0] 
            print(f"\n       {winner} wins this round!") 
            scores[winner] += 1 
        else: 
            print("\n              It's a tie between:", ", ".join(winners)) 
 
         
        print("\n      Current Scores:") 
        for p in scores: 
            print(f"{p}: {scores[p]}") 
 
     
    print("\n    FINAL SCORE") 
    for p in scores: 
        print(f"{p}: {scores[p]}") 
 
    max_final = max(scores.values()) 
    final_winners = [p for p in scores if scores[p] == max_final] 
 
    if len(final_winners) == 1: 
        print(f"\n       {final_winners[0]} WON the game!") 
    else: 
        print("\n              Game is a DRAW between:", ", ".join(final_winners)) 
 
def main_dice():
    while True:
        play_dice()
        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing Dice Game!")
            break
main_dice() 