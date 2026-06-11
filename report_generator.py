import csv
import os
from datetime import datetime

REPORT_FOLDER = 'reports'
LOG_FILE = 'logs/violations.csv'

def create_report_folder():
    if not os.path.exists(REPORT_FOLDER):
        os.makedirs(REPORT_FOLDER)

def generate_report(student_name):
    create_report_folder()
    now = datetime.now()
    report_file = f"{REPORT_FOLDER}/{student_name}_{now.strftime('%Y%m%d_%H%M%S')}.txt"
    
    violations = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            violations = list(reader)

    with open(report_file, 'w') as f:
        f.write("=" * 40 + "\n")
        f.write("EXAM PROCTORING REPORT\n")
        f.write("=" * 40 + "\n")
        f.write(f"Student Name : {student_name}\n")
        f.write(f"Date         : {now.strftime('%Y-%m-%d')}\n")
        f.write(f"Time         : {now.strftime('%H:%M:%S')}\n")
        f.write(f"Total Violations: {len(violations)}\n")
        f.write("=" * 40 + "\n\n")
        
        if violations:
            f.write("Violation Details:\n\n")
            for v in violations:
                f.write(f"Date: {v[0]}\n")
                f.write(f"Time: {v[1]}\n")
                f.write(f"Type: {v[2]}\n")
                f.write(f"Confidence: {v[3]}\n")
                f.write("-" * 20 + "\n")
        else:
            f.write("No violations detected!\n")

    print(f"Report saved: {report_file}")
    return report_file
