import csv
import os
from datetime import datetime

LOG_FILE = 'logs/violations.csv'

def create_log_file():
    if not os.path.exists('logs'):
        os.makedirs('logs')
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                'Date', 
                'Time', 
                'Violation Type', 
                'Confidence'
            ])

def log_violation(violation_type, confidence):
    create_log_file()
    now = datetime.now()
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            now.strftime('%Y-%m-%d'),
            now.strftime('%H:%M:%S'),
            violation_type,
            confidence
        ])
    print(f"Violation logged: {violation_type}")
