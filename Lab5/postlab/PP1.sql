-- Delete existing data
DELETE FROM Enrollment;
DELETE FROM Participant;
DELETE FROM Class;

-- Participant Table
CREATE TABLE IF NOT EXISTS Participant (
    ParticipantNumber INTEGER PRIMARY KEY,
    LastName TEXT NOT NULL,
    FirstName TEXT NOT NULL,
    Address TEXT,
    City TEXT,
    State TEXT,
    PostalCode TEXT,
    TelephoneNumber TEXT,
    DateOfBirth DATE
);

-- Class Table
CREATE TABLE IF NOT EXISTS Class (
    ClassNumber INTEGER PRIMARY KEY,
    ClassDescription TEXT NOT NULL,
    MaxParticipants INTEGER,
    ClassFee REAL
);

-- Enrollment Table
CREATE TABLE IF NOT EXISTS Enrollment (
    ParticipantNumber INTEGER,
    ClassNumber INTEGER,
    ClassDate DATE,
    PRIMARY KEY (ParticipantNumber, ClassNumber, ClassDate),
    FOREIGN KEY (ParticipantNumber) REFERENCES Participant(ParticipantNumber),
    FOREIGN KEY (ClassNumber) REFERENCES Class(ClassNumber)
);

-- Insert sample data into Participant table
INSERT INTO Participant (ParticipantNumber, LastName, FirstName, Address, City, State, PostalCode, TelephoneNumber, DateOfBirth)
VALUES (1, 'Acot', 'Jose', 'Cavite', 'Intramuros', 'MNL', '1400', '555-1234', '1980-01-01'),
       (2, 'Otayde', 'Carl', 'Chicaho', 'Intramuros', 'MNL', '1540', '555-5678', '1990-02-02');

-- Insert sample data into Class table
INSERT INTO Class (ClassNumber, ClassDescription, MaxParticipants, ClassFee)
VALUES (1, 'Hiking Basics', 10, 50.00),
       (2, 'Advanced Biking', 8, 75.00);

-- Insert sample data into Enrollment table
INSERT INTO Enrollment (ParticipantNumber, ClassNumber, ClassDate)
VALUES (1, 1, '2023-10-01'),
       (2, 2, '2023-10-02');

-- List of Participants
SELECT ParticipantNumber, LastName, FirstName, Address, City, State, PostalCode, TelephoneNumber, DateOfBirth
FROM Participant;

-- List of Adventure Classes
SELECT ClassNumber, ClassDescription, MaxParticipants, ClassFee
FROM Class;

-- Participant Enrollments
SELECT p.ParticipantNumber, p.LastName, p.FirstName, c.ClassNumber, c.ClassDescription, e.ClassDate
FROM Participant p
JOIN Enrollment e ON p.ParticipantNumber = e.ParticipantNumber
JOIN Class c ON e.ClassNumber = c.ClassNumber;

-- Class Participants
SELECT e.ClassDate, c.ClassNumber, c.ClassDescription, p.ParticipantNumber, p.LastName, p.FirstName
FROM Class c
JOIN Enrollment e ON c.ClassNumber = e.ClassNumber
JOIN Participant p ON e.ParticipantNumber = p.ParticipantNumber;