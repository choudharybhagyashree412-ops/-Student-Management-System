import sqlite3


# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()


# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL,
    marks REAL NOT NULL
)
""")

conn.commit()


# Add student
def add_student():
    print("\n--- Add Student ---")

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    marks = float(input("Enter marks: "))

    cursor.execute(
        "INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
        (name, age, course, marks)
    )

    conn.commit()
    print("Student added successfully.")


# View students
def view_students():
    print("\n--- Student List ---")

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print(
            "ID:", student[0],
            "| Name:", student[1],
            "| Age:", student[2],
            "| Course:", student[3],
            "| Marks:", student[4]
        )


# Search student
def search_student():
    print("\n--- Search Student ---")

    student_id = int(input("Enter student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("ID:", student[0])
        print("Name:", student[1])
        print("Age:", student[2])
        print("Course:", student[3])
        print("Marks:", student[4])
    else:
        print("Student not found.")


# Update student
def update_student():
    print("\n--- Update Student ---")

    student_id = int(input("Enter student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")
    marks = float(input("Enter new marks: "))

    cursor.execute("""
    UPDATE students
    SET name = ?, age = ?, course = ?, marks = ?
    WHERE id = ?
    """, (name, age, course, marks, student_id))

    conn.commit()

    print("Student updated successfully.")


# Delete student
def delete_student():
    print("\n--- Delete Student ---")

    student_id = int(input("Enter student ID: "))

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully.")
    else:
        print("Student not found.")


# Main menu
def main():
    while True:
        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_student()

            elif choice == "2":
                view_students()

            elif choice == "3":
                search_student()

            elif choice == "4":
                update_student()

            elif choice == "5":
                delete_student()

            elif choice == "6":
                print("Thank you for using Student Management System.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Please enter valid information.")


main()

conn.close()