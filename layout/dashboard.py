# third party
from dash import html
import dash_mantine_components as dmc
import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import dash_mantine_components as dmc
import json
from PIL import Image

# project
from app import app

from layout.pages.upload_page import upload_page_layout
from layout.pages.private_office_page import private_office_layout
# from layout.pages.private_office_page import ministerial_view_layout


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "14rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "16rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

dashboard_layout = private_office_layout


sidebar = html.Div(
    [
        dbc.Row(
            [
                dmc.Title("Box Busters", order=4),
            ]
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Upload", href="/", active="exact"),
                dbc.NavLink("Private Office", href="/PO_view", active="exact"),
                dbc.NavLink(
                    "Ministerial View", href="/ministerial_view", active="exact"
                ),
            ],
            vertical=True,
            pills=True,
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Archive", href="/metrics", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
        html.Hr(),
    ],
    style=SIDEBAR_STYLE,
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return upload_page_layout
    elif pathname == "/PO_view":
        return private_office_layout
    # elif pathname == "/ministerial_view":
    #     return ministerial_view_layout
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised."),
        ],
        className="p-3 bg-light rounded-3",
    )
