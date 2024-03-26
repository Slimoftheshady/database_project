import sqlite3

###############################
# SET UP EMPTY DATABASE
#

def drop_tables(cursor):
    print('Drop tables if they exist')
    query = """
            DROP TABLE IF EXISTS Location;
            DROP TABLE IF EXISTS Employee;
            DROP TABLE IF EXISTS Billing;
            DROP TABLE IF EXISTS Client;
            DROP TABLE IF EXISTS Job;
            DROP TABLE IF EXISTS Team;
            DROP TABLE IF EXISTS Meeting;
            DROP TABLE IF EXISTS EmployeeTeam;
            """
    # Use executescript as there are multiple queries in the same string
    cursor.executescript(query)

def update_pragma(cursor):
    # Update the database to allow foreign keys to enforce referential integrity
    print("Update PRAGMA to support foreign keys")
    query = "PRAGMA foreign_keys = ON"
    cursor.execute(query)

###############################
# CREATE EMPTY TABLES
#
# Create each individual table in the database.
# NOTE: Tables need to be created in correct order to ensure foreign key constraints will work

def create_location_table(cursor):
    print("Create Location Table")
    query = """CREATE TABLE Location (
        location_id INTEGER PRIMARY KEY AUTOINCREMENT,
        state TEXT NOT NULL,
        city TEXT NOT NULL,
        postcode TEXT NOT NULL
        )"""
    cursor.execute(query)

def create_employee_table(cursor):
    print("Create Employee Table")
    query = """CREATE TABLE Employee (
        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        location_id INTEGER NOT NULL,
        FOREIGN KEY(location_id) REFERENCES Location(location_id)
        )"""
    cursor.execute(query)

def create_billing_table(cursor):
    print("Create Billing Table")
    query = """CREATE TABLE Billing (
        billing_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cardnumber INTEGER NOT NULL,
        bank TEXT NOT NULL,
        cvv TEXT NOT NULL
        )"""
    cursor.execute(query)

def create_client_table(cursor):
    print("Create Client Table")
    query = """CREATE TABLE Client (
        client_id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        location_id INTEGER NOT NULL,
        billing_id INTEGER NOT NULL,
        FOREIGN KEY(location_id) REFERENCES Location(location_id)
        FOREIGN KEY(billing_id) REFERENCES Billing(billing_id)
        )"""
    cursor.execute(query)

def create_job_table(cursor):
    print("Create Job Table")
    query = """CREATE TABLE Job (
        job_id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        cost TEXT NOT NULL,
        completion BOOLEAN NOT NULL,
        client_id INTEGER NOT NULL,
        FOREIGN KEY(client_id) REFERENCES Client(client_id)
        )"""
    cursor.execute(query)

def create_team_table(cursor):
    print("Create Team Table")
    query = """CREATE TABLE Team (
        team_id INTEGER PRIMARY KEY AUTOINCREMENT,
        job_id INTEGER NOT NULL,
        FOREIGN KEY(job_id) REFERENCES Job(job_id)
        )"""
    cursor.execute(query)

def create_meeting_table(cursor):
    print("Create Meeting Table")
    query = """CREATE TABLE Meeting (
        meeting_id INTEGER PRIMARY KEY AUTOINCREMENT,
        length INTEGER NOT NULL,
        date TEXT NOT NULL,
        job_id INTEGER NOT NULL,
        FOREIGN KEY(job_id) REFERENCES Job(job_id)
        )"""
    cursor.execute(query)

def create_employeeteam_table(cursor):
    print("Create EmployeeTeam Table")
    query = """CREATE TABLE EmployeeTeam (
        employeeteam_id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER NOT NULL,
        team_id INTEGER NOT NULL,
        FOREIGN KEY(team_id) REFERENCES Team(team_id),
        FOREIGN KEY(employee_id) REFERENCES Employee(employee_id)
        )"""
    cursor.execute(query)

###############################
# CREATE DATABASE
#
# Create the database and populate it with empty tables
# Commit changes to the database so they are saved to the database and close connection.
# Any changes that are made prior to a commit will not be saved until they are committed.
#
def create_db(database_name):
    try:
        # Create connection to database
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        
        drop_tables(cursor)
        update_pragma(cursor)

        create_location_table(cursor)
        create_employee_table(cursor)
        create_billing_table(cursor)
        create_client_table(cursor)
        create_job_table(cursor)
        create_team_table(cursor)
        create_meeting_table(cursor)
        create_employeeteam_table(cursor)

        
        # commit changes to the database so they are saved to the database and close connection
        connection.commit()
        connection.close()
        
        return "success"
    
    except Exception as e:
        print("Error: ", e)
        connection.rollback()
        connection.close()
        return "error"