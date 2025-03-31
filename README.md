# Billing-System-Python

This README.md file provides an overview of your Billing Management System, instructions to set up the project using XAMPP, and how to run it.

🛒 Billing Management System
A Python-based billing system using Tkinter for the UI and MySQL (phpMyAdmin) for database management. This system allows an Admin and Manager to manage billing counters, retrieve sales data, and track daily transactions.

📂 Project Structure
/Billing-Management-System
│── demo.py                  # Main file to start the application
│── main_admin_UI.py         # Admin panel interface
│── main_manager_UI.py       # Manager panel interface
│── counter1.py              # Counter 1 billing interface
│── counter2.py              # Counter 2 billing interface
│── billing_details.py       # Fetches billing data based on date
│── bills_counter1.sql       # Database file for Counter 1
│── bills_counter2.sql       # Database file for Counter 2
│── admin_login.sql          # Admin login details
│── manager_login.sql        # Manager login details
│── README.md                # Project documentation (this file)


⚙️ How to Set Up and Run the Project Using XAMPP
🔹 Step 1: Install Requirements
Download and install XAMPP.
Install Python 3 if not installed.
Install required Python libraries:  "pip install mysql-connector-python tkcalendar"

🔹 Step 2: Start XAMPP Server
Open XAMPP Control Panel.
Click Start on:  1.Apache  2.MySQL

🔹 Step 3: Set Up the MySQL Database
Open phpMyAdmin (http://localhost/phpmyadmin/).
Create a new database billing_python_final.
Import the following SQL files:
           1.  bills_counter1.sql
           2.  bills_counter2.sql
           3.  admin_login.sql
           4.  manager_login.sql


🔹 Step 4: Run the Application
Open the project folder in PyCharm/VS Code.
Run the main file:  "demo.py"

The interface will show Admin & Manager buttons:
Admin Panel:    Click "Admin" → Opens main_admin_UI.py.
Choose Counter 1 (counter1.py) or Counter 2 (counter2.py).
Manager Panel:  Click "Manager" → Opens main_manager_UI.py.
After login, use billing_details.py to fetch sales data.

🛠 Features
✔ Admin Panel to manage counters.
✔ Manager Panel to view sales data.
✔ Billing Counters (Counter 1 & Counter 2).
✔ Daily Sales Fetching using billing_details.py.
✔ MySQL Database Integration for storing transactions.



