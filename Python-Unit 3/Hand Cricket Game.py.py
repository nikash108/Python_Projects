print("Hand Cricket Game") 
score = 0 
comp_numbers = [1,2,3,4,5,6,2,4,1,3,5,6] 
i = 0 
while True: 
    user = int(input("Enter a number (1-6): ")) 
    if user < 1 or user > 6: 
        print("Please enter a number between 1 and 6") 
        continue 
    comp = comp_numbers[i] 
    i = (i + 1) % len(comp_numbers) 
    print("Computer number:", comp) 
    if user == comp: 
        print("You are OUT!") 
        break 
    else: 
        score += user 
        print("Current Score:", score) 
print("Final Score:", score) 