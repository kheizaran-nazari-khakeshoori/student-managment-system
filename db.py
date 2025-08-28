
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "students.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Enable foreign keys
    cur.execute("PRAGMA foreign_keys = ON;")

    # Create tables
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        );
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            credits INTEGER NOT NULL DEFAULT 3
        );
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            student_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            grade REAL, -- optional; can be NULL until graded
            PRIMARY KEY (student_id, course_id),
            FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
            FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
        );
    ''')

    conn.commit()
    conn.close()
