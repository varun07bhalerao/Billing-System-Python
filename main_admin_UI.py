import tkinter as tk
from tkinter import messagebox
import subprocess
import mysql.connector

def open_dashboard():
    login_window.destroy()  # Close login window

    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("600x400")

    tk.Label(dashboard, text="Select Counter:", font=("Arial", 14)).pack(pady=10)

    # Run the database_billing_address.py file when clicking Counter 1
    tk.Button(dashboard, text="Counter 1", command=open_counter1).pack(pady=5)
    tk.Button(dashboard, text="Counter 2", command=open_counter2).pack(pady=5)

    dashboard.mainloop()

def open_counter1():
    subprocess.Popen(["python", "counter1.py"])  # Runs the billing script

def open_counter2():
    subprocess.Popen(["python", "counter2.py"])  # Runs the billing script


def login():
    username = username_entry.get()
    password = password_entry.get()

    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",  # Change if using a different host
            user="root",  # Default user in XAMPP/WAMP
            password="",  # Default password is empty
            database="billing_python_final"
        )
        cursor = conn.cursor()

        # Check username and password
        query = "SELECT * FROM admin_login WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            conn.close()
            open_dashboard()  # Open the dashboard after login
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password")

        conn.close()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")


# Create main window
login_window = tk.Tk()
login_window.title("Admin Login Page")
login_window.geometry("500x300")

# Username Label and Entry
tk.Label(login_window, text="Username:").pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)

# Password Label and Entry
tk.Label(login_window, text="Password:").pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=5)

# Login Button
tk.Button(login_window, text="Login", command=login).pack(pady=10)

# Run the Tkinter event loop
login_window.mainloop()
