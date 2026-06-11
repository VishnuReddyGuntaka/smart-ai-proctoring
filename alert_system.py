import winsound
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from logger import log_violation

def play_alert_sound():
    # Beep sound - frequency, duration
    winsound.Beep(1000, 500)

def show_alert_popup(violation_type, confidence):
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning(
        "⚠️ Violation Detected!",
        f"Violation: {violation_type}\n"
        f"Confidence: {confidence:.2f}\n"
        f"Time: {datetime.now().strftime('%H:%M:%S')}"
    )
    root.destroy()

def trigger_alert(violation_type, confidence):
    # Log violation
    log_violation(violation_type, confidence)
    # Play sound
    play_alert_sound()
    # Show popup
    show_alert_popup(violation_type, confidence)
    print(f"Alert triggered: {violation_type}")
