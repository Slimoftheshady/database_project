##################################################
#
# This code can be used to build Python functions file that will
# insert data into a SQLite database.
# 
# The program reads data from csv files and builds the necessary
# INSERT statements.
#
# The program will create a separate function for each table in the database.
# 
# To use this script:
#   1. Create a folder called Raw Data in your web app folder
#   2. Save the csv files with the data for each table in your database in this folder
#         - one csv file for each table in your database
#         - first row should be the field names
#   3. Save this Python script in the scripts folder of your web app folder
#   3. Update the variables below with the lists of file names and database file etc
#   4. Run the Python script from the web app folder
#
##################################################

##################################################
# FUNCTIONS:
#
#------------------------------
# Build the INSERT queries for the given table
def createQueries(in_name, out_name, table):
  # open output file to add insert statement to
  with open(out_name, 'a') as file_out:
    file_out.write(f"def insert_{table}_data(cursor):\n")
    file_out.write(f"\tprint('Start inserting data into {table} table')\n")

    # open csv file with raw data for table
    with open(f'./Raw Data/{in_name}.csv') as file_in:
      # read first line of csv file to get field names for table
      header = file_in.readline()
      field_names = header.lower().strip().split(',')

      # read in rest of csv file and create list of records  
      records = []
      for line in file_in.readlines():
        record = line.strip().split(',')
        records.append(record)

      # for each record read in, build an INSERT statement and write it to the output file
      for record in records:
        if record[0] != '':
          line = f"\tcursor.execute('''INSERT INTO {table} ("
          line += ', '.join(field_names)
          line += ') VALUES ('
          for field in record:
            # if value is a digit add value, otherwise put quotation marks around string
            if field.isdigit():
              line += f'{field.strip()}, '
            else:
              line += f'"{field.strip()}", '
            out_line = f"{line[:-2]})''')\n" # need to strip last ', ' from each line
          file_out.write(out_line)

    file_out.write(f"\tprint('Finish inserting data into {table} table')\n\n")

#------------------------------
# This adds the code for the start of the CGI program
def startFile(out_file):
  with open(out_file, 'w') as f_out:
    script = 'import sqlite3\n\n'
    f_out.write(script)
  
#------------------------------
# This adds the code for the end of the CGI program
def endFile(out_file):
  with open(out_file, "a") as f_out:
    script = 'def insert_table_data(database_name):\n'
    script += '\ttry:\n'
    script += '\t\tconnection = sqlite3.connect(database_name)\n'
    script += '\t\tcursor = connection.cursor()\n\n'''
    
    for table in tables:
      script += f'\t\tinsert_{table}_data(cursor)\n'

    script += '\n\t\tconnection.commit()\n'
    script += '\t\tconnection.close()\n\n'
    script += '\t\treturn "Data inserted successfully"\n'
    script += '\texcept Exception as e:\n'
    script += '\t\tprint("Error: ", e)\n'
    script += '\t\tconnection.rollback()\n'
    script += '\t\tconnection.close()\n'
    script += '\t\treturn "Error inserting data into database"'
    f_out.write(script)


##################################################
#
# CHANGE THE FOLLOWING LINES TO PRODUCE YOUR CGI PROGRAM TO INSERT DATA INTO YOUR DATABASE:
#
# These are the input csv files for your data.
# NOTE:
#   1. all csv files need to be in a folder called Raw Data
#   2. the first line in each csv file should contain the name of each field
#   3. tables need to be entered in the correct order to ensure referential integrity
#      That is, tables that are referenced by other tables need to be entered first
in_files = ["Location", "Employee", "Billing", "Client", "Job", "Team", "Meeting", "EmployeeTeam"]

# These are the tables that each csv file corresponds to
# NOTE: the order of tables must match the order of the csv files
tables = ["Location", "Employee", "Billing", "Client", "Job", "Team", "Meeting", "EmployeeTeam"]

# The name of the database
database = "AuzEngineering.db"

# The name of the python file that you will create
out_file = "insert_db_data.py"
#
##################################################

##################################################
#
# This code calls the functions to run the program!
#
startFile(out_file)
for i in range(len(in_files)):
  createQueries(in_files[i], out_file, tables[i])
endFile(out_file)
