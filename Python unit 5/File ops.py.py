import csv 
import os 
FILE_NAME = "students.csv" 
def create_file(): 
    if not os.path.exists(FILE_NAME): 
        with open(FILE_NAME, "w", newline="") as file: 
            writer = csv.writer(file) 
            writer.writerow(["Name", "Age", "Course"]) 
 
def add_student(): 
    name = input("Enter Name: ").title() 
    age = input("Enter Age: ") 
    course = input("Enter Course: ").title() 
 
    with open(FILE_NAME, "a", newline="") as file: 
        writer = csv.writer(file) 
        writer.writerow([name, age, course]) 
 
    print("Student added successfully!") 
 
def view_students(): 
    with open(FILE_NAME, "r") as file: 
        reader = csv.reader(file) 
        print("\n--- Student Records ---") 
        for row in reader: 
            print(row) 
 
def search_student(): 
    name = input("Enter name to search: ").title() 
    found = False 
 
    with open(FILE_NAME, "r") as file: 
        reader = csv.reader(file) 
        for row in reader: 
            if row and row[0] == name: 
                print("Record Found:", row) 
                found = True 
                break 
 
    if not found: 
        print("Student not found") 
 
def delete_student(): 
    name = input("Enter name to delete: ").title() 
    rows = [] 
 
    with open(FILE_NAME, "r") as file: 
        reader = csv.reader(file) 
        rows = list(reader) 
 
    with open(FILE_NAME, "w", newline="") as file: 
        writer = csv.writer(file) 
        for row in rows: 
            if row and row[0] != name: 
                writer.writerow(row) 
 
    print("Record deleted if existed") 
 
def main(): 
    create_file() 
 
    while True: 
        print("\n1. Add Student") 
        print("2. View Students") 
        print("3. Search Student") 
        print("4. Delete Student") 
        print("5. Exit") 
 
        choice = input("Enter choice: ") 
 
        if choice == '1': 
            add_student() 
        elif choice == '2': 
            view_students() 
        elif choice == '3': 
            search_student() 
        elif choice == '4': 
            delete_student() 
        elif choice == '5': 
            break 
        else: 
            print("Invalid choice") 
 
main() 