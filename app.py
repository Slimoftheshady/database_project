from bottle import route, run, template, request, static_file
import sqlite3
import scripts.create_database as create_database
import scripts.insert_db_data as insert_db_data
import queries

##################################################
#
# Constants
#
DATABASE_FILE = 'AuzEngineering.db'

##################################################
#
# Routes for each page
#
# Home page
@route('/')
def index():
    return template('index')
    #out = template('index') + template('sidebar')
    #return out

# Queries to create a fresh database and insert data into the database
@route('/create_db')
def create_db():
    title = "Creating Empty Data"
    success = create_database.create_db(DATABASE_FILE)
    return  template('create_database', success=success)

@route('/insert_data')
def insert_data():
    title = "Inserting Data into Database"
    result = insert_db_data.insert_table_data(DATABASE_FILE)
    return  template('insert_data', success=result)
 
# Hard coded queries that always return the same results
#employees
@route('/select_all_employees')
def select_all_employees():
    title = 'Employees'
    query = queries.SELECT_ALL_EMPLOYEES
    #return get_template(query, title, description)
    check = template('sidebar') + get_template(query, title)
    return check
#jobs
@route('/select_all_jobs')
def select_all_areas():
    title = 'Jobs'
    query = queries.SELECT_ALL_JOBS
    check = template('sidebar') + get_template(query, title)
    return check
#clients
@route('/select_all_clients')
def select_all_clients():
    title = 'Clients'
    query = queries.SELECT_ALL_CLIENTS
    check = template('sidebar') + get_template(query, title)
    return check
#meetings
@route('/select_meetings')
def select_meetings():
    title = 'Meetings'
    query = queries.SELECT_MEETINGS
    check = template('sidebar') + get_template(query, title)
    return check

#billings
@route('/select_billings')
def select_billings():
    title = 'Billings'
    query = queries.SELECT_BILLINGS
    check = template('sidebar') + get_template(query, title)
    return check

#teams
@route('/select_teams')
def select_teams():
    title = 'Teams'
    query = queries.SELECT_TEAMS
    check = template('sidebar') + get_template(query, title)
    return check

 # Queries that require the use of a form.

''' query to insert new data
@route('/select_new_data')
def select_new_data():
    return template('newdata')

@route('/newdata', method='POST')
def newdata():
    title = 'Client'
    
    location = request.forms.get("loc")
    state = request.forms.get("state")
    city = request.forms.get("city")
    postcode = request.forms.get("post")

    values = {'location': location,'state': state,'city':city,'postcode':postcode}
    query = queries.SELECT_DATA
    check = template('sidebar') + get_template_with_parameters(query, values, title)
    return check
 '''

# Static CSS Files
@route('/static/<filename>')
def static(filename):
    return static_file(filename, root='./static')

##################################################
#
# Helper functions to run queries for each page
#
def get_db_connection():
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row
    return connection

def run_query(query):
    return run_query_with_parameters(query, {})

def run_query_with_parameters(query, values):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(query, values)
    result = cursor.fetchall()

    connection.close()

    return result

def get_template(query, title='Query Results', description='This page shows the results of a query'):
    return get_template_with_parameters(query, {}, title, description)

def get_template_with_parameters(query, values, title='Query Results', description='This page shows the results of a query'):
    result = run_query_with_parameters(query, values)
    if len(result) > 0:
        page = template('results', title=title, description=description, records=result)
    else:
        page = template('no_results', title=title, description=description)
    return page


##################################################
#
# Run the web server to serve up the pages
#
run(host='localhost', port=8080, reloader=True, debug=True)