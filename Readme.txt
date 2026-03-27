# Billing System using Python and MySQL

This project is a billing system implemented using Python with Tkinter for the GUI and MySQL for the database. The system has an admin login interface that allows access to two billing counters for generating bills and saving them in the database.

## Project Structure
- `main_admin_UI.py`: The main file to execute the application.
- `counter1.py` and `counter2.py`: These files represent the two billing counters.
- `admin_login.sql`, `bills_counter1.sql`, and `bills_counter2.sql`: The SQL files for database setup.

---

## How to Run the Project
### Step 1: Install XAMPP
- Download and install XAMPP from [https://www.apachefriends.org/index.html](https://www.apachefriends.org/index.html)

### Step 2: Start MySQL and Apache Servers
- Open XAMPP Control Panel.
- Start **Apache** and **MySQL** services.
- Click on the **Admin** button of MySQL to open phpMyAdmin.

### Step 3: Create a New Database
- In phpMyAdmin, create a new database named **`billing_python_final`**.
- Import the three SQL files:
  - `admin_login.sql`
  - `bills_counter1.sql`
  - `bills_counter2.sql`

### Step 4: Install Required Libraries
- Make sure to have Python installed.
- Install the required library using the following command:
```bash
pip install mysql-connector-python
```

### Step 5: Run the Project
- Open the project directory in your command prompt or terminal.
- Run the main file using:
```bash
python main_admin_UI.py
```

---

## Usage
- The login credentials can be found in the `admin_login` table of the database.
- After a successful login, you can select either **Counter 1** or **Counter 2** to generate bills.
- The bills will be saved in the respective tables **bills_counter1** and **bills_counter2**.

## Screenshots
- Login Page
- Admin Dashboard
- Billing Counters

## Future Enhancements
- Enhanced data validation and security features.
- Additional payment gateway integration.
- Inventory management system.

## License
This project is open-source and free to use.

