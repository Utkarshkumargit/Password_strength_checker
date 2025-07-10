# ==================== LOGIC SECTION ====================

import tkinter as tk
from tkinter import messagebox
import re

def is_strong_password(password):
    length = len(password) >= 8
    digit = re.search(r"\d", password)
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    return all([length, digit, upper, lower, symbol])

# ==================== GUI SECTION ====================

def check_strength():
    password = entry.get()
    if is_strong_password(password):
        result = "✅ Strong Password 💪"
        result_label.config(text=result, fg="green")
    else:
        result = (
            "❌ Weak Password\n\n"
            "Check for:\n"
            "• 8+ characters\n"
            "• A-Z\n"
            "• a-z\n"
            "• 0-9\n"
            "• special symbols"
        )
        result_label.config(text=result, fg="red")
    messagebox.showinfo("Password Strength", result)

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("450x300")
root.configure(bg="#1e1e2f")

tk.Label(root, text="Enter Password:", font=("Helvetica", 13, "bold"), bg="#1e1e2f", fg="#ffffff").pack(pady=15)
entry = tk.Entry(root, show="*", width=30, font=("Helvetica", 12))
entry.pack(pady=10)

tk.Button(root, text="Check Strength", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", command=check_strength).pack(pady=10)
result_label = tk.Label(root, text="", font=("Helvetica", 11), bg="#1e1e2f", fg="white")
result_label.pack(pady=10)

root.mainloop()

