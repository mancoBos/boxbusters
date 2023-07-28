import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_iconify import DashIconify

import pandas as pd

from layout.functions.prep_data import *
from app import app

test_file = "SofS approved a sprint on Unblocking GP Data for researchers. This will commence on Monday 31st of July with the first workshop in the sprint. The initial phase will comprise of 5 workshops, detailed below, to gather as much information about concerns, considerations, and ideas that different stakeholders have on this issue. "

# def pop_up_box(file):
formatted_text = process_word_to_correct_format(test_file)
summary_note = create_summary_note_function(formatted_text)
additional_context = additional_context_function(formatted_text)
[file_title, SRO_name, due_date] = extract_relevant_info(formatted_text)
    # return 

private_office_layout = html.Div(
    [
        html.Br(),
        dmc.Title("private office view goes here", order=2),
        html.Br(),
       dmc.Accordion(
    children=[
        dmc.AccordionItem(
            [
                dmc.AccordionControl(file_title, icon=DashIconify(
                        icon="tabler:circle-check",
                        color=dmc.theme.DEFAULT_COLORS["green"][6],
                        width=20,
                    ),),
                dmc.AccordionPanel(html.Div([
                    dbc.Row([
                        dbc.Col([
                            html.Div("SRO: "+ SRO_name)
                        ]),
                        dbc.Col([
                            html.Div("Due: "+due_date)
                        ])
                    ]),
                    summary_note, ])
                ),
            ],
            value="customization",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl("Flexibility"),
                dmc.AccordionPanel(
                    "Configure temp appearance and behavior with vast amount of settings or overwrite any part of "
                    "component styles "
                ),
            ],
            value="flexibility",
        ),
    ],
)
    ]
)

