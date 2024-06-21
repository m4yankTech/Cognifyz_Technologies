import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%I:%M:%S %p')  # Include AM/PM indicator
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Update every second

# Create the main window
root = tk.Tk()
root.title("Creative Digital Clock")
root.geometry("300x150")

# Create a gradient background
background_canvas = tk.Canvas(root, width=300, height=150)
background_canvas.pack()
background_canvas.create_rectangle(0, 0, 300, 150, fill="#339066", outline="")

# Create a sleek frame
frame = tk.Frame(root, bg="#000033")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create a label for displaying the time
clock_label = tk.Label(frame, font=('Arial', 40, 'bold'), bg="#004053", fg="#FFD800")
clock_label.pack(pady=20)

# Call the update_time function to initialize the clock
update_time()

# Run the Tkinter event loop
root.mainloop()
