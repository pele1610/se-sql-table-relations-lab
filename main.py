# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')


pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
schema = pd.read_sql("""SELECT * FROM sqlite_master""", conn)
print(schema)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql("""
SELECT employees.firstName, employees.lastName
FROM employees
JOIN offices ON employees.officeCode = offices.officeCode
WHERE offices.city = "Boston"
""", conn)
print(df_boston)

# STEP 2
# Replace None with your code
df_zero_emp = df_zero_emp = pd.read_sql("""
SELECT offices.officeCode
FROM offices
LEFT JOIN employees ON offices.officeCode = employees.officeCode
WHERE employees.employeeNumber IS NULL
""", conn)
print(df_zero_emp)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql("""
SELECT employees.firstName, employees.lastName, offices.city, offices.state
FROM employees
LEFT JOIN offices ON employees.officeCode = offices.officeCode
ORDER BY employees.firstName, employees.lastName
""", conn)
print(df_employee)

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql("""
SELECT customers.contactFirstName, customers.contactLastName, customers.phone, customers.salesRepEmployeeNumber
FROM customers
LEFT JOIN orders ON customers.customerNumber = orders.customerNumber
WHERE orders.orderNumber IS NULL
ORDER BY customers.contactLastName
""", conn)
print(df_contacts)

# STEP 5
# Replace None with your code
df_payment = pd.read_sql("""
SELECT customers.contactFirstName, customers.contactLastName, payments.amount, payments.paymentDate
FROM customers
JOIN payments ON customers.customerNumber = payments.customerNumber
ORDER BY CAST(payments.amount AS REAL) DESC
""", conn)
print(df_payment)

# STEP 6
# Replace None with your code
df_credit = None

# STEP 7
# Replace None with your code
df_product_sold = None

# STEP 8
# Replace None with your code
df_total_customers = None

# STEP 9
# Replace None with your code
df_customers = None

# STEP 10
# Replace None with your code
df_under_20 = None

conn.close()