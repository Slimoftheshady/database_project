<!DOCTYPE html>
<html>
    <head>
        <title>Auz Engineering Database</title>
        <link type="text/css" href="/static/main_style.css" rel="stylesheet">
    </head>
    <body>
        <div class="he">
            <ul>
              <li><a href="/">Home</a></li>
              <li><a href="/select_all_jobs">Jobs</a></li>
              <li><a href="/select_all_employees">Employees</a></li>
              <li><a href="/select_all_clients">Clients</a></li>
              <li><a href="#">Data Entry</a></li>
            </ul>
            </div>



            <div class="query">
                <div class="query_form">
                    <form action="/newdata" method="post">
        
                        <label for="field">Enter Location_id:</label>
                        <input type="text" id="loc" name="loc" required/><br />
      
                        <label for="value">Enter State:</label>
                        <input type="text" id="state" name="state" required/><br />

                        <label for="value">Enter city:</label>
                        <input type="text" id="city" name="city" required/><br />

                        <label for="value">Enter postcode:</label>
                        <input type="text" id="post" name="post" required/><br />

                        <input type="submit" value="Enter">
                    </form>
                </div>
      

    </body>
</html>