#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

# Create a connection to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="leme"
)

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Create a table
create_table_query = """
    CREATE TABLE bookings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        customer_name VARCHAR(255),
        date DATE,
        status VARCHAR(50)
    )
"""
cursor.execute(create_table_query)
cnx.commit()

# Insert a booking into the table
insert_booking_query = """
    INSERT INTO bookings (customer_name, date, status)
    VALUES (%s, %s, %s)
"""
booking_data = ("John Doe", "2023-06-16", "Confirmed")
cursor.execute(insert_booking_query, booking_data)
cnx.commit()

# Retrieve all bookings from the table
select_bookings_query = "SELECT * FROM bookings"
cursor.execute(select_bookings_query)
bookings = cursor.fetchall()
for booking in bookings:
    print(booking)

# Close the cursor and connection
cursor.close()
cnx.close()


# In[5]:


import mysql.connector

# Create a connection to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="leme"
)

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Check if the connection is open
if cnx.is_connected():
    print("Connection to the database is open.")

# Execute the query
select_latest_booking_query = "SELECT * FROM bookings ORDER BY date DESC LIMIT 1"
cursor.execute(select_latest_booking_query)
latest_booking = cursor.fetchone()
print(latest_booking)

# Close the cursor and connection
cursor.close()
cnx.close()


# In[11]:


import mysql.connector

# Create a connection to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="leme"
)

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Define the bookings data
bookings_data = [
    ("John Doe", "2023-06-16", "Confirmed"),
    ("Jane Smith", "2023-06-17", "Pending"),
    ("Michael Johnson", "2023-06-18", "Confirmed")
]

# Define the SQL query
insert_booking_query = "INSERT INTO bookings (customer_name, date, status) VALUES (%s, %s, %s)"

# Insert multiple bookings
cursor.executemany(insert_booking_query, bookings_data)
cnx.commit()

# Print a success message
print("Bookings added successfully!")

# Close the cursor and connection
cursor.close()
cnx.close()


# In[12]:


import mysql.connector

# Create a connection to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="leme"
)

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Create the AddBooking stored procedure
create_procedure_query = """
    CREATE PROCEDURE AddBooking(
        IN customer_name VARCHAR(255),
        IN booking_date DATE,
        IN booking_status VARCHAR(50),
        OUT inserted_id INT
    )
    BEGIN
        INSERT INTO bookings (customer_name, date, status)
        VALUES (customer_name, booking_date, booking_status);
        
        SET inserted_id = LAST_INSERT_ID();
    END
"""
cursor.execute(create_procedure_query)
cnx.commit()

# Insert a booking and retrieve the inserted ID
customer_name = "John Doe"
booking_date = "2023-06-16"
booking_status = "Confirmed"

add_booking_procedure = "CALL AddBooking(%s, %s, %s, @booking_id)"
cursor.execute(add_booking_procedure, (customer_name, booking_date, booking_status))
cnx.commit()

# Retrieve the inserted ID from the session variable
cursor.execute("SELECT @booking_id")
inserted_id = cursor.fetchone()[0]

# Print the inserted booking ID
print("Inserted Booking ID:", inserted_id)

# Close the cursor and connection
cursor.close()
cnx.close()


# In[14]:


import mysql.connector

# Create a connection to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="leme"
)

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Define the start and end dates for the range
start_date = "2023-06-16"
end_date = "2023-06-18"

# Define the SQL query
select_bookings_query = "SELECT * FROM bookings WHERE date BETWEEN %s AND %s"

# Execute the query with the date range parameters
cursor.execute(select_bookings_query, (start_date, end_date))

# Fetch all the bookings
bookings = cursor.fetchall()

# Print the retrieved bookings
for booking in bookings:
    print(booking)

# Close the cursor and connection
cursor.close()
cnx.close()


# In[16]:


import mysql.connector

# Create a connection to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="leme"
)

# Create a cursor object to interact with the database
cursor = cnx.cursor()
# UpdateBooking Procedure
update_procedure_query = """
    CREATE PROCEDURE UpdateBooking(
        IN booking_id INT,
        IN new_status VARCHAR(50)
    )
    BEGIN
        UPDATE bookings
        SET status = new_status
        WHERE id = booking_id;
    END
"""
cursor.execute(update_procedure_query)
cnx.commit()

# CancelBooking Procedure
cancel_procedure_query = """
    CREATE PROCEDURE CancelBooking(IN booking_id INT)
    BEGIN
        UPDATE bookings
        SET status = 'Cancelled'
        WHERE id = booking_id;
    END
"""
cursor.execute(cancel_procedure_query)
cnx.commit()


# In[ ]:




