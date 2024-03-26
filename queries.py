# This file contains all the queries that are used in the web application.

SELECT_ALL_EMPLOYEES = '''SELECT Employee.firstname || ' ' || Employee.lastname AS Name, Employee.phone AS Phone, Employee.email as Email, Employee.address AS Address, Location.postcode AS Postcode, Location.city AS City, Location.state AS State FROM Employee, Location
                        WHERE Employee.location_id = Location.location_id
                        ORDER BY Employee.firstname ASC


                    '''

SELECT_ALL_JOBS = '''SELECT Job.job_id AS 'Job Number', Client.firstname ||' '||Client.lastname AS Client, SUBSTRING(Job.description, 1, 100) AS 'Job Description', Job.cost AS 'Cost ($)', Job.completion AS Completion FROM Job, Client
                        WHERE Job.client_id = Client.client_id
                        ORDER BY Job.job_id ASC
                    '''

SELECT_ALL_CLIENTS = '''SELECT Client.firstname || ' ' || Client.lastname AS Name, Client.phone AS Phone, Client.email as Email, Client.address AS Address, Location.postcode AS Postcode, Location.city AS City, Location.state AS State FROM CLient, Location
                        WHERE Client.location_id = Location.location_id
                        ORDER BY Client.firstname ASC
                    '''

SELECT_MEETINGS = '''SELECT Meeting.date AS Date, Meeting.length AS 'Length (minutes)', SUBSTRING(Job.description, 1, 100) AS 'Job Description', Client.firstname ||' '|| Client.lastname AS Client FROM Meeting, Job, Client
                        WHERE Meeting.job_id = Job.job_id
                        AND Job.client_id = Client.client_id
                        ORDER BY Client.firstname ASC
                    '''
SELECT_BILLINGS = '''SELECT Client.firstname ||' '|| Client.lastname AS Client, Billing.bank AS Bank, Billing.cardnumber AS 'Card Number', Billing.cvv AS CVV FROM Client, Billing
                        WHERE Billing.billing_id = Client.billing_id
                        ORDER BY Client.firstname ASC
                    '''
SELECT_TEAMS = '''SELECT Job.job_id AS 'Job Number', employee.firstname ||' '|| employee.lastname AS Employee, client.firstname ||' '|| client.lastname AS Client FROM Employee, Client, Job, EmployeeTeam, Team
                        WHERE Job.client_id = client.client_id
                        AND Job.job_id = Team.job_id
                        AND Team.team_id = EmployeeTeam.team_id
                        AND Employee.employee_id = EmployeeTeam.employee_id
                        ORDER BY Job.job_id ASC
                '''

#query to insert new data
''' 
SELECT_DATA = INSERT INTO Location (location_id, state, city, postcode) VALUES ('location', "state", "city", "postcode")
                 '''


