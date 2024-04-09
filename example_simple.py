import cx_Oracle

# Create a connection using Kerberos authentication
connection = cx_Oracle.connect("/", mode=cx_Oracle.SYSDBA)

# Create a cursor
cursor = connection.cursor()

# Execute a query
cursor.execute("SELECT * FROM your_table")

# Fetch all rows from the last executed statement
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()