from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'blood_bank_db'

# Initialize MySQL
mysql = MySQL(app)

# Routes

@app.route('/')
def home():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM doctor")
    doctor_data = cursor.fetchall()
    cursor.close()

    return render_template('db.html', doctor_data=doctor_data)

@app.route('/donor')
def donor():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM donor")
    donor_data = cursor.fetchall()
    cursor.close()

    return render_template('db1.html', donor_data=donor_data)

@app.route('/donor_form')
def donor_form():
    return render_template('db1.html')

@app.route('/submit_donor', methods=['POST'])
def submit_donor():
    if request.method == 'POST':
        # Extract donor data from the form
        donor_name = request.form['donor_name']
        donor_addr = request.form['donor_addr']
        donor_phno = request.form['donor_phno']
        bp = request.form['bp']
        weight = request.form['weight']
        dob = request.form['dob']
        iron_content = request.form['iron_content']
        don_amt = request.form['don_amt']
        blood_type = request.form['blood_type']
        doctor_id = request.form['doctor_id']

        # Check if the required blood is available in blood_availability
        cursor = mysql.connection.cursor()
        availability_query = "SELECT * FROM blood_availability WHERE blood_type = %s AND amount >= %s"
        cursor.execute(availability_query, (blood_type, don_amt))
        available_data = cursor.fetchall()

        if available_data:
            # Print details from blood_availability
            print("\nBlood Availability Details:")
            print("Donor ID\tBlood Type\tAmount\t\tExpiry Date")
            print("----------------------------------------------")
            for row in available_data:
                print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")

            # Update blood_availability by decreasing the amount donated
            update_query = "UPDATE blood_availability SET amount = amount - %s WHERE blood_type = %s AND amount >= %s"
            cursor.execute(update_query, (don_amt, blood_type, don_amt))
            mysql.connection.commit()
        else:
            # If blood is not available, provide details of donors with the required blood type
            donors_query = "SELECT * FROM donor WHERE blood_type = %s"
            cursor.execute(donors_query, (blood_type,))
            donors_data = cursor.fetchall()

            if donors_data:
                print("\nDonors with Required Blood Type:")
                print("Donor ID\tName\t\tAddress\t\tPhone")
                print("----------------------------------------")
                for donor in donors_data:
                    print(f"{donor[0]}\t{donor[1]}\t\t{donor[2]}\t\t{donor[3]}")
            else:
                print(f"\nNo donors found with blood type {blood_type}")

        # Insert donor data into the 'donor' table
        insert_query = "INSERT INTO donor (donor_name, donor_addr, donor_phno, bp, weight, dob, iron_content, don_amt, blood_type, doctor_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (donor_name, donor_addr, donor_phno, bp, weight, dob, iron_content, don_amt, blood_type, doctor_id))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('donor'))

@app.route('/patient', methods=['GET', 'POST'])
def patient():
    if request.method == 'POST':
        # Extract patient data from the form
        username = request.form['username']
        password = request.form['password']
        blood_type = request.form['blood_type']

        # Check if the amount of blood is available in blood_availability
        cursor = mysql.connection.cursor()
        availability_query = "SELECT * FROM blood_availability WHERE blood_type = %s AND amount > 0"
        cursor.execute(availability_query, (blood_type,))
        available_data = cursor.fetchall()

        if available_data:
            # Print details from blood_availability
            print("\nBlood Availability Details:")
            print("Donor ID\tBlood Type\tAmount\t\tExpiry Date")
            print("----------------------------------------------")
            for row in available_data:
                print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}\t\t{row[3]}")

            # Update blood_availability by decreasing the amount donated
            update_query = "UPDATE blood_availability SET amount = amount - 1 WHERE blood_type = %s AND amount > 0 LIMIT 1"
            cursor.execute(update_query, (blood_type,))
            mysql.connection.commit()
        else:
            # If blood is not available, provide details of donors with the required blood type
            donors_query = "SELECT * FROM donor WHERE blood_type = %s"
            cursor.execute(donors_query, (blood_type,))
            donors
