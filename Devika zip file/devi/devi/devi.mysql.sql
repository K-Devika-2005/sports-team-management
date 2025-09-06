-- CREATE  table devi;
USE devi;
CREATE TABLE sports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(15) NOT NULL,
	address TEXT NOT NULL,
    emergency_contact_name VARCHAR(100) NOT NULL,
    emergency_contact_number VARCHAR(15) NOT NULL,
    selected_sport VARCHAR(50) NOT NULL,
    sport_level VARCHAR(50),
    skill_level VARCHAR(100),
    previous_experience TEXT,
    medical_info TEXT,
    allergies TEXT,
    medical_conditions TEXT,
    medications TEXT,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
select * from sports;