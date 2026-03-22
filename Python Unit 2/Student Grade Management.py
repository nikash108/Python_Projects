num_students = int(input("Enter number of students: ")) 
for i in range(num_students): 
    print("\n--- Student", i + 1, "---" )
    name = input("Enter student name: ") 
    num_subjects = int(input("Enter number of subjects: ")) 
    total = 0 
    for j in range(num_subjects): 
        mark = float(input(f"Enter mark for subject {j + 1}: ")) 
        total += mark 
    average = total / num_subjects 
    print("\nStudent Name:", name) 
    print("Total Marks:", total) 
    print("Average:", round(average, 2)) 
    if average >= 90: 
        grade = "A" 
    elif average >= 75: 
        grade = "B" 
    elif average >= 50: 
        grade = "C" 
else: 
        grade = "Fail" 
print("Grade:", grade) 