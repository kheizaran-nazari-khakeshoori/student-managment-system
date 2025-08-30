
from db import init_db
import repository as repo

def print_table(rows, headers):
    if not rows:
        print("(no results)")
        return
    # compute widths
    widths = [len(h) for h in headers]
    for r in rows:
        for i, col in enumerate(r):
            widths[i] = max(widths[i], len(str(col)))
    # header
    line = " | ".join(h.ljust(widths[i]) for i, h in enumerate(headers))
    sep = "-+-".join("-" * widths[i] for i in range(len(headers)))
    print(line)
    print(sep)
    # rows
    for r in rows:
        print(" | ".join(str(col).ljust(widths[i]) for i, col in enumerate(r)))

def menu():
    print("\n=== Student Management System ===")
    print("1. Add student")
    print("2. List students")
    print("3. Update student")
    print("4. Delete student")
    print("5. Add course")
    print("6. List courses")
    print("7. Delete course")
    print("8. Enroll student in course")
    print("9. Set grade for student in course")
    print("10. List enrollments")
    print("11. Student report & average")
    print("0. Exit")

def main():
    init_db()
    while True:
        menu()
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                name = input("Student name: ").strip()
                age = int(input("Age: ").strip())
                sid = repo.add_student(name, age)
                print(f"Added student with id {sid}.")
            elif choice == "2":
                rows = repo.list_students()
                print_table(rows, ["id", "name", "age"])
            elif choice == "3":
                sid = int(input("Student id: ").strip())
                name = input("New name (leave blank to skip): ").strip()
                age_text = input("New age (leave blank to skip): ").strip()
                name_val = name if name else None
                age_val = int(age_text) if age_text else None
                repo.update_student(sid, name=name_val, age=age_val)
                print("Student updated.")
            elif choice == "4":
                sid = int(input("Student id to delete: ").strip())
                repo.delete_student(sid)
                print("Student deleted.")
            elif choice == "5":
                title = input("Course title: ").strip()
                credits = int(input("Credits (default 3): ") or "3")
                cid = repo.add_course(title, credits)
                print(f"Added course with id {cid}.")
            elif choice == "6":
                rows = repo.list_courses()
                print_table(rows, ["id", "title", "credits"])
            elif choice == "7":
                cid = int(input("Course id to delete: ").strip())
                repo.delete_course(cid)
                print("Course deleted.")
            elif choice == "8":
                sid = int(input("Student id: ").strip())
                cid = int(input("Course id: ").strip())
                repo.enroll(sid, cid)
                print("Enrollment saved.")
            elif choice == "9":
                sid = int(input("Student id: ").strip())
                cid = int(input("Course id: ").strip())
                grade = float(input("Grade (0-100): ").strip())
                repo.set_grade(sid, cid, grade)
                print("Grade recorded.")
            elif choice == "10":
                rows = repo.list_enrollments()
                print_table(rows, ["student_id", "student", "course_id", "course", "grade"])
            elif choice == "11":
                sid = int(input("Student id: ").strip())
                rows = repo.student_report(sid)
                print_table(rows, ["course", "credits", "grade"])
                avg = repo.student_average_grade(sid)
                print(f"Average grade: {avg:.2f}")
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
