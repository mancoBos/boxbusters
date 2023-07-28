# import logging
import os
import json

# third party
import dash
import dash_bootstrap_components as dbc

# import dash_auth

# Keep this out of source code repository - save in a file or a database
# VALID_USERNAME_PASSWORD_PAIRS = json.loads(os.getenv("users"))
PREFIX_URL = os.environ.get("PREFIX_URL", "/")

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.LUX,
        # lato_font
    ],
    url_base_pathname=PREFIX_URL,
)

# auth = dash_auth.BasicAuth(app)

server = app.server
app.config.suppress_callback_exceptions = True
