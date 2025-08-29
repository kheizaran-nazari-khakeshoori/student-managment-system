
from typing import Optional
from db import get_connection

# -------- Students --------
def add_student(name: str, age: int) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id

def list_students() -> list:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, age FROM students ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return rows

def update_student(student_id: int, name: Optional[str]=None, age: Optional[int]=None) -> None:
    conn = get_connection()
    cur = conn.cursor()
    if name is not None and age is not None:
        cur.execute("UPDATE students SET name=?, age=? WHERE id=?", (name, age, student_id))
    elif name is not None:
        cur.execute("UPDATE students SET name=? WHERE id=?", (name, student_id))
    elif age is not None:
        cur.execute("UPDATE students SET age=? WHERE id=?", (age, student_id))
    conn.commit()
    conn.close()

def delete_student(student_id: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()

# -------- Courses --------
def add_course(title: str, credits: int = 3) -> int:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO courses (title, credits) VALUES (?, ?)", (title, credits))
    conn.commit()
    new_id = cur.lastrowid
    conn.close()
    return new_id

def list_courses() -> list:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, credits FROM courses ORDER BY id")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_course(course_id: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM courses WHERE id=?", (course_id,))
    conn.commit()
    conn.close()

# -------- Enrollments & Grades --------
def enroll(student_id: int, course_id: int) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO enrollments (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
    conn.commit()
    conn.close()

def set_grade(student_id: int, course_id: int, grade: float) -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE enrollments SET grade=? WHERE student_id=? AND course_id=?", (grade, student_id, course_id))
    if cur.rowcount == 0:
        # If not enrolled yet, enroll and set grade
        cur.execute("INSERT INTO enrollments (student_id, course_id, grade) VALUES (?, ?, ?)", (student_id, course_id, grade))
    conn.commit()
    conn.close()

def list_enrollments() -> list:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT e.student_id, s.name, e.course_id, c.title, e.grade
        FROM enrollments e
        JOIN students s ON s.id = e.student_id
        JOIN courses c ON c.id = e.course_id
        ORDER BY e.student_id, e.course_id
    ''')
    rows = cur.fetchall()
    conn.close()
    return rows

def student_report(student_id: int) -> list:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT c.title, c.credits, e.grade
        FROM enrollments e
        JOIN courses c ON c.id = e.course_id
        WHERE e.student_id=?
        ORDER BY c.title
    ''', (student_id,))
    rows = cur.fetchall()
    conn.close()
    return rows

def student_average_grade(student_id: int) -> float:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT AVG(grade) FROM enrollments WHERE student_id=? AND grade IS NOT NULL", (student_id,))
    avg = cur.fetchone()[0]
    conn.close()
    return avg if avg is not None else 0.0
