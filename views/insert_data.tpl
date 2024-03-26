<!DOCTYPE html>
<html>
    <head>
        <title>Auz Engineering Database</title>
        <link type="text/css" href="/static/results_style.css" rel="stylesheet">
    </head>

    <body>
        <header>
            <p><a href="/">Return to Home Page</a></p>
        </header>

        <h1>Inserting data into empty database</h1>

	    % if 1 == 1:
        %       description = "Database inserted successfully"

		<p class="{{ success }}"><strong>{{ description }}</strong></p>

        <footer>
            <p><a href="/">Return to Home Page</a></p>
        </footer>
    </body>
</html>