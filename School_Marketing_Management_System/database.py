"""SQLite database functions for the School Marketing Management System."""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("school_marketing.db")

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id TEXT PRIMARY KEY,
                full_name TEXT NOT NULL,
                age INTEGER NOT NULL CHECK(age BETWEEN 5 AND 120),
                programme TEXT NOT NULL,
                phone TEXT,
                interest TEXT NOT NULL
            )
        """)

def add_student(student_id, full_name, age, programme, phone, interest):
    student_id, full_name = str(student_id).strip(), str(full_name).strip()
    programme, phone, interest = str(programme).strip(), str(phone).strip(), str(interest).strip()
    if not student_id or not full_name or not programme or not interest:
        raise ValueError("Student ID, name, programme and interest are required.")
    try:
        age = int(age)
    except (TypeError, ValueError):
        raise ValueError("Age must be a whole number.")
    if not 5 <= age <= 120:
        raise ValueError("Age must be between 5 and 120.")
    try:
        with get_connection() as connection:
            connection.execute(
                """INSERT INTO students (student_id, full_name, age, programme, phone, interest)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (student_id, full_name, age, programme, phone, interest))
        return True
    except sqlite3.IntegrityError:
        return False

def get_all_students():
    with get_connection() as connection:
        return connection.execute("SELECT * FROM students ORDER BY full_name").fetchall()

def get_student(student_id):
    with get_connection() as connection:
        return connection.execute(
            "SELECT * FROM students WHERE student_id = ?", (str(student_id).strip(),)
        ).fetchone()

def update_student(student_id, full_name=None, age=None, programme=None, phone=None, interest=None):
    existing = get_student(student_id)
    if existing is None:
        return False
    values = {
        "full_name": existing["full_name"] if full_name is None else str(full_name).strip(),
        "age": existing["age"] if age is None else age,
        "programme": existing["programme"] if programme is None else str(programme).strip(),
        "phone": existing["phone"] if phone is None else str(phone).strip(),
        "interest": existing["interest"] if interest is None else str(interest).strip(),
    }
    try:
        values["age"] = int(values["age"])
    except (TypeError, ValueError):
        raise ValueError("Age must be a whole number.")
    if not 5 <= values["age"] <= 120:
        raise ValueError("Age must be between 5 and 120.")
    if not values["full_name"] or not values["programme"] or not values["interest"]:
        raise ValueError("Name, programme and interest cannot be blank.")
    with get_connection() as connection:
        connection.execute(
            """UPDATE students SET full_name=?, age=?, programme=?, phone=?, interest=?
               WHERE student_id=?""",
            (values["full_name"], values["age"], values["programme"], values["phone"],
             values["interest"], str(student_id).strip()))
    return True

def delete_student(student_id):
    with get_connection() as connection:
        cursor = connection.execute("DELETE FROM students WHERE student_id = ?",
                                     (str(student_id).strip(),))
        return cursor.rowcount > 0
