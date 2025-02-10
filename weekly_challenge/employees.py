import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('employees.db')
cursor = connection.cursor()

# Create employees table
cursor.execute("""
               CREATE TABLE IF NOT EXISTS employees(
               id INT PRIMARY KEY,
               name TEXT,
               salary NUMERIC)""")

# Insert row values in our table
cursor.execute("DELETE FROM employees") # Clears existing data
employees_data = [(1,'John','45000'),(2,'Elma','60000'),(3, 'Enock','75000'),(4, 'Preston','50000')]
cursor.executemany("INSERT INTO employees (id, name, salary) VALUES(?,?,?)", employees_data)
print("Rows inserted successfully")

# Display data from the employees 
cursor.execute("SELECT * FROM employees")
results = cursor.fetchall()
print("Employees Table Data:", results)



# A query to retrieve employees with salary > 50000
cursor.execute("""
               SELECT name, salary
               FROM employees
               WHERE salary > 50000;
               """)
great_salary = cursor.fetchall()
print("Employees earning more than 50000:",great_salary)
