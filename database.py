import sqlite3
import os
from datetime import datetime

DB_FILE = 'proctoring.db'

def create_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            exam_date TEXT NOT NULL
        )
    ''')
    
    # Violations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS violations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            violation_type TEXT NOT NULL,
            confidence REAL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            FOREIGN KEY (student_id) 
            REFERENCES students (id)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database created successfully!")

def add_student(name, email):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    now = datetime.now()
    cursor.execute('''
        INSERT INTO students (name, email, exam_date)
        VALUES (?, ?, ?)
    ''', (name, email, now.strftime('%Y-%m-%d')))
    student_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return student_id

def add_violation(student_id, violation_type, confidence):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    now = datetime.now()
    cursor.execute('''
        INSERT INTO violations 
        (student_id, violation_type, confidence, date, time)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        student_id,
        violation_type,
        confidence,
        now.strftime('%Y-%m-%d'),
        now.strftime('%H:%M:%S')
    ))
    conn.commit()
    conn.close()
    print(f"Violation added: {violation_type}")

def get_violations(student_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM violations 
        WHERE student_id = ?
    ''', (student_id,))
    violations = cursor.fetchall()
    conn.close()
    return violations
