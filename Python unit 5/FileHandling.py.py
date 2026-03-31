def add_record(): 
    with open("students.txt", "a") as file: 
        name = input("Enter Name: ") 
        roll = input("Enter Roll No: ") 
        marks = input("Enter Marks: ") 
 
        file.write(f"{name},{roll},{marks}\n") 
        print("   Record Added Successfully!") 
 
def view_records(): 
    try: 
        with open("students.txt", "r") as file: 
            data = file.readlines() 
            if not data: 
                print("    No records found!") 
                return 
 
            print("\n         Student Records:") 
            for line in data: 
                name, roll, marks = line.strip().split(",") 
                print(f"Name: {name}, Roll: {roll}, Marks: {marks}") 
 
    except FileNotFoundError: 
        print("    File not found!") 
 
def search_record(): 
    name_search = input("Enter name to search: ").lower() 
 
    try: 
        with open("students.txt", "r") as file: 
            found = False 
            for line in file: 
                name, roll, marks = line.strip().split(",") 
                if name.lower() == name_search: 
                    print(f"    Found → Name: {name}, Roll: {roll}, Marks: {marks}") 
                    found = True 
 
            if not found: 
                print("  Record not found!") 
 
    except FileNotFoundError: 
        print("    File not found!") 
 
def main(): 
    while True: 
        print("\n   STUDENT RECORD SYSTEM") 
        print("1. Add Record") 
        print("2. View Records") 
        print("3. Search Record") 
        print("4. Exit") 
 
        choice = input("Enter choice: ") 
 
        if choice == "1": 
            add_record() 
        elif choice == "2": 
            view_records() 
        elif choice == "3": 
            search_record() 
        elif choice == "4": 
            print("          Exiting program...") 
            break 
        else: 
            print("    Invalid choice!") 
 
main() 