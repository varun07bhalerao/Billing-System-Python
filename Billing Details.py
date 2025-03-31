import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
import subprocess

def fetch_billing_data():
    entered_date = date_entry.get().strip()

    if not entered_date:
        messagebox.showerror("Input Error", "Please select a valid date.")
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="billing_python_final"
        )
        cursor = conn.cursor()

        query = """
            SELECT bill_no, customer_name, phone, items, total_price, 'Counter 1' AS counter_number, employee_name
            FROM bills_counter1 WHERE DATE(bill_date) = %s
            UNION ALL
            SELECT bill_no, customer_name, phone, items, total_price, 'Counter 2' AS counter_number, employee_name
            FROM bills_counter2 WHERE DATE(bill_date) = %s
        """

        cursor.execute(query, (entered_date, entered_date))
        data = cursor.fetchall()

        total_query = """
            SELECT SUM(total_price) FROM bills_counter1 WHERE DATE(bill_date) = %s
            UNION ALL
            SELECT SUM(total_price) FROM bills_counter2 WHERE DATE(bill_date) = %s
        """

        cursor.execute(total_query, (entered_date, entered_date))
        total_sales_data = cursor.fetchall()

        conn.close()

        total_sales = sum(sale[0] for sale in total_sales_data if sale[0] is not None)

        if not data:
            messagebox.showinfo("No Entries", f"No entries found on {entered_date}")
            return

        display_data(data, total_sales)

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

def display_data(data, total_sales):
    for row in tree.get_children():
        tree.delete(row)

    for row in data:
        tree.insert("", "end", values=row)

    total_sales_label.config(text=f"Total Sales: ₹{total_sales}")

def logout():
    subprocess.Popen(["python", "demo.py"])  # Run demo.py
    billing_window.destroy()  # Close the billing window

# Create main window
billing_window = tk.Tk()
billing_window.title("Billing Details")
billing_window.geometry("1300x800")
billing_window.configure(bg="#F5F5F5")  # Light background color
billing_window.state("zoomed")

# Create a frame for the Logout button (for proper alignment)
top_frame = tk.Frame(billing_window, bg="#F5F5F5")
top_frame.pack(fill="x", pady=10, padx=20)

# Logout Button (Placed inside the top frame, aligned to the right)
logout_button = tk.Button(
    top_frame, text="Logout", command=logout, font=("Arial", 12, "bold"),
    bg="#E74C3C", fg="white", padx=10, pady=5
)
logout_button.pack(side="right")

# Date Entry Label & Calendar Widget
tk.Label(billing_window, text="Select Date:", font=("Arial", 12, "bold"), bg="#F5F5F5").pack(pady=5)
date_entry = DateEntry(billing_window, width=12, background="blue", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd", showweeknumbers=False, selectmode='day', year=2025, month=3, day=31)
date_entry.pack(pady=5)

# Fetch Data Button
tk.Button(billing_window, text="Fetch Data", command=fetch_billing_data, font=("Arial", 12, "bold"), bg="#3498DB", fg="white", padx=10, pady=5).pack(pady=10)

# Table to display results
columns = ("Bill No", "Customer Name", "Phone", "Items", "Total Price", "Counter", "Employee Name")
tree = ttk.Treeview(billing_window, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(expand=True, fill="both", padx=20, pady=10)

# Total Sales Label
total_sales_label = tk.Label(billing_window, text="Total Sales: ₹0", font=("Arial", 14, "bold"), bg="#F5F5F5", fg="#2C3E50")
total_sales_label.pack(pady=10)

# Run the Tkinter event loop
billing_window.mainloop()