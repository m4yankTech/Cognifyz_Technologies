import re
import tkinter as tk
from tkinter import messagebox


def evaluate_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))

    criteria_met = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        digit_criteria,
        special_char_criteria
    ])

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should contain at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character.")

    return {
        "strength": strength,
        "feedback": feedback
    }


def show_password_strength():
    password = entry.get()
    result = evaluate_password_strength(password)
    strength_message = f"Password Strength: {result['strength']}\n"
    feedback_message = "\n".join(result['feedback'])
    messagebox.showinfo("Password Strength", strength_message + feedback_message)


# Create the main window
root = tk.Tk()
root.title("Password Strength Evaluator")

# Create and place the label, entry, and button
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=40)
entry.pack(pady=10)

button = tk.Button(root, text="Evaluate", command=show_password_strength)
button.pack(pady=10)

# Run the application
root.mainloop()
