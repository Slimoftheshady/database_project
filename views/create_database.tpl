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

        <h1>Creating Empty Database</h1>

	    % if success == "success":
        %       description = "Database created successfully"
        % else:
        %       description = "Database creation failed"
        % end
		<p class="{{ success }}"><strong>{{ description }}</strong></p>

        <footer>
            <p><a href="/">Return to Home Page</a></p>
        </footer>
    </body>
</html>
