-- Create a database for the blood bank management system
CREATE DATABASE IF NOT EXISTS blood_bank_db;
USE blood_bank_db;

-- Table: doctor
CREATE TABLE doctor (
    doctor_id INT PRIMARY KEY,
    doctor_name VARCHAR(100),
    doctor_hospital VARCHAR(100),
    doctor_phno INT
);
INSERT INTO  doctor VALUES (1,'Ann','abc hospital','9723752953');

-- Table: donor
CREATE TABLE donor (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_name VARCHAR(100),
    donor_addr VARCHAR(100),
    donor_phno VARCHAR(100),
    bp VARCHAR(100),
    weight VARCHAR(100),
    dob VARCHAR(100),
    iron_content VARCHAR(100),
    don_amt VARCHAR(100),
    blood_type VARCHAR(5),
    doctor_id INT,
    FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id)
);

-- Table: blood_bank
CREATE TABLE blood_bank (
    bank_id INT AUTO_INCREMENT PRIMARY KEY,
    bank_name VARCHAR(100),
    bank_addr VARCHAR(100)
);

-- Table: blood_availability
CREATE TABLE blood_availability (
    donor_id INT,
    blood_type VARCHAR(5),
    amount VARCHAR(100),
    expiry DATE,
    FOREIGN KEY (donor_id) REFERENCES donor(donor_id)
);

-- Table: patient
CREATE TABLE patient (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100),
    blood_type VARCHAR(5),
    req_amt VARCHAR(100),
    patient_phno VARCHAR(100),
    patient_addr VARCHAR(100),
    hospital_addr VARCHAR(100)
);
