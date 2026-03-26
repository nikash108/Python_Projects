quiz = {
    "What is 10 + 5?": "15",
    "Capital of Tamil Nadu?": "Chennai",
    "Python supports OOP? (yes/no)": "yes",
    "9 * 3 = ?": "27"
}

attempts = []

def play():
    score = 0

    for q in quiz:
        user = input(q + " ").strip().lower()

        if user == quiz[q].lower():
            print("✅ Correct\n")
            score += 1
        else:
            print(f"❌ Wrong! Answer: {quiz[q]}\n")

    return score

def show_result(score):
    total = len(quiz)
    percent = (score / total) * 100

    print(f"\nYour Score: {score}/{total}")
    print(f"Percentage: {percent:.2f}%")

    if percent >= 75:
        print("🔥 Topper Level")
    elif percent >= 50:
        print("👍 Average")
    else:
        print("📚 Study more bro")

def track_progress(score):
    attempts.append(score)

    print("\n📊 Attempt History:", attempts)
    print("🏆 Best Score:", max(attempts))

def string_fun():
    name = input("\nEnter your name: ")
    print("Uppercase:", name.upper())
    print("Reversed:", name[::-1])

def retry():
    choice = input("\nTry again? (yes/no): ").lower()

    if choice == "yes":
        main()
    elif choice == "no":
        print("👋 Bye!")
    else:
        print("Invalid input!")
        retry()

def main():
    print("\n=== Student Quiz Tracker ===")

    score = play()
    show_result(score)
    track_progress(score)
    string_fun()
    retry()

main()