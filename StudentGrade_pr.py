# Student Grades Program

# Create a dictionary to store student names and grades
students = {}

while True:
    print("\n--- Student Grade Menu ---")
    print("1. Add a new student")
    print("2. Update a student's grade")
    print("3. Print all students and grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        if name in students:
            print(f"{name} already exists! Use update option instead.")
        else:
            students[name] = grade
            print(f"Added {name} with grade {grade}")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input(f"Enter new grade for {name}: ")
            students[name] = grade
            print(f"Updated {name}'s grade to {grade}")
        else:
            print(f"{name} not found!")

    elif choice == "3":
        if students:
            print("\n--- Student Grades ---")
            for name, grade in students.items():
                print(f"{name}: {grade}")
        else:
            print("No students found!")

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter 1-4.")
