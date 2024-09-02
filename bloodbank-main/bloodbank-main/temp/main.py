import mysql.connector

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="blood_bank_db"
)

# Create a cursor object to interact with the database
cursor = db_connection.cursor()

# Example: Select data from the doctor table
select_doctor_query = "SELECT * FROM doctor"
cursor.execute(select_doctor_query)
doctor_data = cursor.fetchall()

if doctor_data:
    print("\nDoctor Information:")
    print("ID\tName\t\tAddress\t\tPhone")
    print("--------------------------------")
    for doctor in doctor_data:
        print(f"{doctor[0]}\t{doctor[1]}\t\t{doctor[2]}\t\t{doctor[3]}")
else:
    print("No doctor data found.")

# Example: Insert data into the donor table
insert_donor_query = """
INSERT INTO donor (donor_name, donor_addr, donor_phno, bp, weight, dob, iron_content, don_amt, blood_type, doctor_id)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""
donor_data = ("John Doe", "Address", "123-456-7890", "120/80", "70 kg", "1990-01-01", "Normal", "200 ml", "O+", 1)
cursor.execute(insert_donor_query, donor_data)
db_connection.commit()
print("\nDonor added successfully.")

# Example: Fetch data from the blood_availability table
select_blood_availability_query = "SELECT * FROM blood_availability"
cursor.execute(select_blood_availability_query)
availability_data = cursor.fetchall()

if availability_data:
    print("\nBlood Availability:")
    print("Donor ID\tBlood Type\tAmount\t\tExpiry Date")
    print("----------------------------------------------")
    for row in availability_data:
        print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
else:
    print("No blood availability data found.")

# Close the cursor and database connection
cursor.close()
db_connection.close()
