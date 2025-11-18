"""
Student Course Management System using Python Sets
-------------------------------------------------

This project demonstrates how sets can be used to manage unique student lists,
compare enrollments between two courses, and find common or exclusive students.

Features:
- Maintain unique student names
- Find students in both courses (intersection)
- Find students only in one course (difference)
- Find all students (union)
- Find students not common to both courses (symmetric difference)
"""

# -----------------------------
#  INITIAL STUDENT SETS
# -----------------------------

course_A = {"Rohan", "Neha", "Amit", "Sara"}
course_B = {"Amit", "Vikram", "Neha", "John"}


# -----------------------------
#  DISPLAY FUNCTION
# -----------------------------

def show_sets():
    """Display the students in each course."""
    print("\n--- Course Enrollment ---")
    print("Course A Students:", course_A)
    print("Course B Students:", course_B)
    print("----------------------------")


# -----------------------------
#  MENU LOOP
# -----------------------------

while True:
    print("\n===== STUDENT COURSE MANAGEMENT =====")
    print("1. Show Student Lists")
    print("2. Show Students in BOTH Courses (Intersection)")
    print("3. Show ALL Students (Union)")
    print("4. Show Students ONLY in Course A (A - B)")
    print("5. Show Students ONLY in Course B (B - A)")
    print("6. Show Students NOT Common (Symmetric Difference)")
    print("7. Add Student to Course A")
    print("8. Add Student to Course B")
    print("9. Exit")

    choice = input("Enter choice: ").strip()

    # Show sets
    if choice == "1":
        show_sets()

    # Intersection
    elif choice == "2":
        print("\nStudents in BOTH courses (A ∩ B):")
        print(course_A & course_B)

    # Union
    elif choice == "3":
        print("\nALL Students (A ∪ B):")
        print(course_A | course_B)

    # A - B
    elif choice == "4":
        print("\nStudents ONLY in Course A (A - B):")
        print(course_A - course_B)

    # B - A
    elif choice == "5":
        print("\nStudents ONLY in Course B (B - A):")
        print(course_B - course_A)

    # Symmetric Difference
    elif choice == "6":
        print("\nStudents NOT common in both courses (A Δ B):")
        print(course_A ^ course_B)

    # Add to Course A
    elif choice == "7":
        new_student = input("Enter student name to add to Course A: ").strip()
        course_A.add(new_student)
        print("✔ Student added to Course A.")

    # Add to Course B
    elif choice == "8":
        new_student = input("Enter student name to add to Course B: ").strip()
        course_B.add(new_student)
        print("✔ Student added to Course B.")

    # Exit
    elif choice == "9":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice! Please choose from 1-9.")
