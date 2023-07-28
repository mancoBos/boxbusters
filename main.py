# std
import os
import logging

# third party
from dash import html, dcc

# project
from app import app
from layout.dashboard import dashboard_layout, sidebar


logging.info("Setting main layout")


# main layout of the index page
app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>PODS Dashboard</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""

app.layout = html.Div([dcc.Location(id="url"), dashboard_layout], style = {'margin':'25px'})


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", debug=False, port=os.environ.get("PORT", 8080))
    