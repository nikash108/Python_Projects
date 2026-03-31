import random 
import time 
categories = { 
"Programming Languages": ["python", "java", "javascript", "golang"], 
"Game Titles": ["minecraft", "fortnite", "valorant", "pubg"], 
"Computer Parts": ["processor", "motherboard", "graphics", "ram"] 
} 
def choose_word():
    category = random.choice(list(categories.keys()))
    word = random.choice(categories[category])
    return word, category
def display_word(guessed, word):
    return " ".join([letter if letter in guessed else "_" for letter in word]) 
def get_attempts(level):
    if level == "easy":
        return 6
    elif level == "medium":
        return 4
    else:
        return 3 
 
def play_hangman(): 
    word, category = choose_word() 
    guessed_letters = set() 
    hint_used = False 
    score = 0 
 
    print("\nHANGMAN GAME (Tech Edition)") 
    level = input("Choose difficulty (easy/medium/hard): ").lower() 
    attempts = get_attempts(level) 
 
    print("Category:", category) 
    print("Hint: Word length is", len(word)) 
 
    while attempts > 0: 
        print("\nWord:", display_word(guessed_letters, word)) 
        print("Attempts left:", attempts) 
        print("Guessed:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None") 
 
        choice = input("Enter letter or type 'hint': ").lower() 
 
        if choice == "hint": 
            if not hint_used: 
                remaining = [l for l in word if l not in guessed_letters] 
                if remaining: 
                    hint_letter = random.choice(remaining) 
                    print("Hint letter:", hint_letter) 
                    hint_used = True 
                    attempts -= 1 
                else: 
                    print("No letters left to reveal!") 
            else: 
                print("Hint already used!") 
            continue 
 
        if len(choice) != 1 or not choice.isalpha(): 
            print("Enter a valid letter!") 
            continue 
 
        if choice in guessed_letters: 
            print("Already guessed!") 
            continue 
 
        guessed_letters.add(choice) 
 
        if choice not in word: 
            attempts -= 1 
            print("Wrong guess!") 
        else: 
            print("Correct!") 
 
        if all(letter in guessed_letters for letter in word): 
            score += attempts * 10 
            print("\nYou WON! Word was:", word) 
            print("Score gained:", score) 
            return score 
 
    print("\nYou LOST! Word was:", word) 
    return 0 
 
def main_hangman(): 
    total_score = 0 
 
    while True: 
        total_score += play_hangman() 
        again = input("\nPlay again? (yes/no): ").lower() 
        if again != "yes": 
            print("\nFinal Score:", total_score) 
            print("Thanks for playing!") 
            break 
 
main_hangman() 