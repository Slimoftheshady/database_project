<!DOCTYPE html>
<html>
    <head>
        <title>Auz Engineering Database</title>
        <link type="text/css" href="/static/results_style.css" rel="stylesheet">
    </head>


    <body>
        <div class="contain">
        <h1>{{ title }}</h1>
        <table>
            <tr>
                % for field in records[0].keys():
                <th> {{ field }} </th>
                % end
            </tr>
            % for record in records:
            <tr>
                % for field in record:
                <td>{{ field }}</td>
                % end
            </tr>
            % end
        </table>
        </div>
    </body>
</html>