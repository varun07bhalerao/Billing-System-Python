import tkinter as tk
import subprocess

def open_admin():
    subprocess.Popen(["python", "main_admin_UI.py"])
def open_manager():
    subprocess.Popen(["python", "main_manager_UI.py"])

# Create main window
main_window = tk.Tk()
main_window.title("Billing System Login")
main_window.geometry("400x300")

# Heading Label
tk.Label(main_window, text="Select User Type", font=("Arial", 16, "bold")).pack(pady=20)

# Admin Button
tk.Button(main_window, text="Admin", font=("Arial", 14), command=open_admin, width=15).pack(pady=10)

# Manager Button
tk.Button(main_window, text="Manager", font=("Arial", 14), command=open_manager, width=15).pack(pady=10)

# Run the Tkinter event loop
main_window.mainloop()
