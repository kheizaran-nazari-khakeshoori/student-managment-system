
# Student Management System (Python + SQLite)

A simple CLI project to manage **students**, **courses**, **enrollments**, and **grades** using Python and SQLite.
Perfect for learning SQL + Python and for a first portfolio project.

## Features
- Add, list, update, and delete **students**
- Add, list, and delete **courses**
- **Enroll** students in courses
- **Set grades** for enrollments
- View a **student report** and **average grade**
- Uses **SQLite** (no server needed), pure Python standard library

## Project Structure
```
student-management-system/
├── app.py           # CLI menu & interaction
├── repository.py    # All database operations (CRUD)
├── db.py            # DB connection & schema initialization
├── students.db      # Created at first run
└── README.md
```

## Requirements
- Python 3.8+
- No external packages needed (uses Python standard library)

## How to Run
```bash
# 1) Clone or download this repo
# 2) From the project folder, run:
python app.py
```

A `students.db` file will be created automatically on first run.

## Example Commands (inside the app)
- Add student → enter name & age
- Add course → enter title & credits
- Enroll student → provide student id & course id
- Set grade → provide student id, course id, and the grade (0–100)
- Student report → shows all courses and the average grade

## Notes
- SQLite enables **foreign keys**; deleting a student also removes enrollments.
- You can safely delete `students.db` to reset data (the schema will be recreated).
- For a GUI or web version later, consider **Tkinter** (desktop) or **Flask**/**Django** (web).

## License
MIT — feel free to use and modify for learning purposes.
