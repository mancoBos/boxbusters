import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

import pandas as pd

from layout.functions.prep_data import *
from layout.functions.report_functions_and_variables import *
from layout.pages.upload_page import upload_page_layout
from app import app

from layout.functions.chatgptprocess import test_file, additional_context

word_image_path = 'data/word.png'

#comment these out
# test_file = "tester replace with chatgpt output"
# additional_context = "original text"

formatted_text = process_word_to_correct_format(test_file)
summary_note = create_summary_note_function(formatted_text)
[file_title, SRO_name, due_date] = extract_relevant_info(formatted_text)

edited_summary_note = html.Div(
    id="summary-edited-version", style={"whiteSpace": "pre-line"})


###PRIVATE OFFICE PAGE
def pop_up_review_box():
    
    return [   dbc.Row(
                            [   dbc.Col([html.Div(id = 'icon_of_interest')]),
                                dbc.Col([html.Div("SRO: " + SRO_name)]),
                                dbc.Col([html.Div("Due: " + due_date)]),
                                dbc.Col([html.A("View original document", href='https://healthsharedservice-my.sharepoint.com/:t:/r/personal/ali_mittens_dhsc_gov_uk/Documents/Documents/git/box-busters/data/uploads/example_embed.txt?csf=1&web=1&e=Oy7Qt2', target="_blank")])
                           ]
                        ),              
                                        html.B("Summary Note:"),
                                        dcc.Textarea(
                                            id="summary-edit-box",
                                            value=summary_note,
                                            persistence=True,
                                            persistence_type="local",
                                            style={"width": "100%", 'height':100},
                                        ),
                                        html.Br(),
                                        html.B("Additional Context"),
                                        dcc.Textarea(
                                            id="additional-context-edit-box",
                                            value=additional_context,
                                            persistence=True,
                                            persistence_type="local",
                                            style={"width": "100%"},
                                        ),
                                        html.Br(),
                                        html.Div ('Do you agree with the priority rating?'),
                                        dcc.Dropdown(
    [
        {
            "label": html.Span(
                [
                    red_icon,
                    html.Span("High", style={'font-size': 15, 'padding-left': 10}),
                ], style={'align-items': 'center', 'justify-content': 'center'}
            ),
            "value": "High",
        },
        {
            "label": html.Span(
                [
orange_icon,
                    html.Span("Medium", style={'font-size': 15, 'padding-left': 10}),
                ], style={'align-items': 'center', 'justify-content': 'center'}
            ),
            "value": "Medium",
        },
        {
            "label": html.Span(
                [
                   green_icon,
                   html.Span("Low", style={'font-size': 15, 'padding-left': 10}),
                ], style={'align-items': 'center', 'justify-content': 'center'}
            ),
            "value": "Low",
        },
    ],
    value="High", id = 'priority_dropdown'

),
                                        dbc.Button(
                                            "Save and Submit",
                                            id="close-pop-up",
                                            className="ms-auto",
                                            n_clicks=0,
                                        ),
                                    ]


def item_box():

    return dmc.AccordionItem(
        [
            dmc.AccordionControl(
                file_title,
                icon=red_icon
            ),
            dmc.AccordionPanel(
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col([html.Div("SRO: " + SRO_name)]),
                                dbc.Col([html.Div("Due: " + due_date)]),
                                dbc.Col([dbc.Button("Review", id="open-pop-up", n_clicks=0),]),
                            ]
                        ),
                        html.Br(),
                        edited_summary_note,
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle(file_title)),
                                dbc.ModalBody(pop_up_review_box()
                                ),
                            ],
                            id="pop-up-modal",
                            size="xl",
                            style={"max-width": "none", "height": "90%"},
                            is_open=False,
                        ),
                    ]
                )
            ),
        ],
        value="customisation",
    )

today_date = pd.Timestamp("today").strftime("%m/%d/%Y")

private_office_box_processing_tab = html.Div([
    html.Br(),
    html.B("Items to be reviewed for boxing:"),
    dmc.Accordion(
    children=[
        item_box(),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "Correspondence from Antonia Romeo Permanent Sec",
                    icon = orange_icon
                ),
                dmc.AccordionPanel(
                    "Correspondence about how our team is definitely going to win the hackathon"
                ),
            ],
            value="flexibility",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "For Info: Update on Red Box System",
                    icon = green_icon,
                ),
                dmc.AccordionPanel(
                    "Everyone will be using this system soon!"
                ),
            ],
            value="example",
        ),
    ],
)])

ministerial_view_tab_summary = html.Div(id = "saved-output-for-minister-summary")
ministerial_view_tab_context = html.Div(id = "saved-output-for-minister-context")
ministerial_response_tab_summary = html.Div(id = "saved-output-for-ministerial-response-summary")
ministerial_response_tab_context = html.Div(id = "saved-output-for-ministerial-response-context")
ministerial_response_comments = html.Div(id = 'ministerial_comments')


###MINISTERIAL VIEW TAB

def pop_up_review_box_minister():
    
    return [   dbc.Row(
                            [   dbc.Col([red_icon]),
                                dbc.Col([html.Div("SRO: " + SRO_name)]),
                                dbc.Col([html.Div("Due: " + due_date)]),
                                 dbc.Col([html.A("View original document", href='https://healthsharedservice-my.sharepoint.com/:t:/r/personal/ali_mittens_dhsc_gov_uk/Documents/Documents/git/box-busters/data/uploads/example_embed.txt?csf=1&web=1&e=Oy7Qt2', target="_blank")])
                           ]
                        ),              
                                         html.Br(),
        html.Div("Summary: "),
        html.Div(ministerial_view_tab_summary),
        html.Br(),
        html.Div("Additional Context: "),
                html.Div(ministerial_view_tab_context),
                html.Br(),
                html.Div("Please add any comments or questions:"),
                dcc.Textarea(
                                            id="ministers-comments-input",
                                            value="",
                                            persistence=True,
                                            persistence_type="local",
                                            style={"width": "100%", 'height':100},
                                        ),
                                        html.Br(),
                                        dbc.Row([
                                            dbc.Col([
dbc.Button(
                                            "Remove from box-no further action required",
                                            id="no-action-required",
                                            className="ms-auto",
                                            n_clicks=0,
                                             color="info"
                                        ),
                                            ], width={"size": 6, "offset": 3},), 
                                            dbc.Col([
 dbc.Button(
                                            "Return Comments to Private Office",
                                            id="close-pop-up-minister",
                                            className="ms-auto",
                                            color="primary",
                                            n_clicks=0,
                                        ),  
                                            ]),
                                
                                        ])
                                        
                                    ]


def item_box_minister():

    return dmc.AccordionItem(
        [
            dmc.AccordionControl(
                file_title,
                icon=red_icon
            ),
            dmc.AccordionPanel(
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col([html.Div("SRO: " + SRO_name)]),
                                dbc.Col([html.Div("Due: " + due_date)]),
                                dbc.Col([dbc.Button("Review", id="open-pop-up-minister", n_clicks=0)]),
                            ]
                        ),                
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle(file_title)),
                                dbc.ModalBody(pop_up_review_box_minister()
                                ),
                            ],
                            id="pop-up-modal-minister",
                            size="xl",
                            style={"max-width": "none", "height": "90%"},
                            is_open=False,
                        ),
                    ]
                )
            ),
        ],
        value="customization",
    )



#### MINISTERIAL RETURNS TAB
def pop_up_review_box_ministerial_returns():
    
    return [   dbc.Row(
                            [   dbc.Col([red_icon]),
                                dbc.Col([html.Div("SRO: " + SRO_name)]),
                                dbc.Col([html.Div("Due: " + due_date)]),
                                 dbc.Col([html.A("View original document", href='https://healthsharedservice-my.sharepoint.com/:t:/r/personal/ali_mittens_dhsc_gov_uk/Documents/Documents/git/box-busters/data/uploads/example_embed.txt?csf=1&web=1&e=Oy7Qt2', target="_blank")])
                           ]
                        ),              
                                         html.Br(),
        html.Div("Summary: "),
        html.Div(ministerial_response_tab_summary),
        html.Br(),
        html.Div("Additional Context: "),
                html.Div(ministerial_response_tab_context),
                html.Br(),
                dmc.Alert(
                    html.Div(ministerial_response_comments), title="Ministerial Comments:",
                )    ,                                   
                  html.Br(),
                                       
dbc.Button(
                                            "Action taken - remove from list",
                                            id="close-pop-up-ministerial-return",
                                            className="ms-auto",
                                            n_clicks=0,
                                        )]
                                            
                                      


def item_box_ministerial_returns():

    return dmc.AccordionItem(
        [
            dmc.AccordionControl(
                file_title,
                icon=red_icon
            ),
            dmc.AccordionPanel(
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col([html.Div("SRO: " + SRO_name)]),
                                dbc.Col([html.Div("Due: " + due_date)]),
                                dbc.Col([dbc.Button("Review", id="open-pop-up-ministerial-return", n_clicks=0)]),
                            ]
                        ),                
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle(file_title)),
                                dbc.ModalBody(pop_up_review_box_ministerial_returns()
                                ),
                            ],
                            id="pop-up-modal-ministerial-return",
                            size="xl",
                            style={"max-width": "none", "height": "90%"},
                            is_open=False,
                        ),
                    ]
                )
            ),
        ],
        value="customization",
    )


ministerial_returns_layout = html.Div([
       html.Br(),
        html.B("Returned items with further actions:"),
     dmc.Accordion(
    children=[
        item_box_ministerial_returns(),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "Proposed Response to Media: Issue of the Day",
                    icon=red_icon
                ),
                dmc.AccordionPanel(
                    "Are you happy with this press release?"
                ),
            ],
            value="example1",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "Policy Options for Proposed Change to Animal Welfare Laws",
                    icon=red_icon
                ),
                dmc.AccordionPanel(
                    "How to handle badgers with TB and the associated costs"
                ),
            ],
            value="example12",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "For info: Gen AI Uses in Government",
                    icon=green_icon
                ),
                dmc.AccordionPanel(
                    "Look at the cool things we can do!"
                ),
            ],
            value="example3",
        ),
        ])
    

])



##### MINISTERIAL VIEW TAB
ministerial_view_layout = html.Div([
    html.Br(),
        html.B("Outstanding items to be reviewed:"),
    
dmc.Accordion(
    children=[
        item_box_minister(),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "Correspondence from Ben Norman, Deputy Chief Fire",
                    icon=orange_icon
                ),
                dmc.AccordionPanel(
                    "The world is on fire!"
                ),
            ],
            value="example1",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "For Info: Upcoming Departmental Hackathon",
                    icon=green_icon
                ),
                dmc.AccordionPanel(
                    "We are running a series of hackathons in the department to help find innovative tech solutions for pressing issues"
                ),
            ],
            value="example2",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "For info: Updated National Recommendations on J-TAC Applications",
                    icon=green_icon
                ),
                dmc.AccordionPanel(
"Some new national guidelines you may be interested in!"                ),
            ],
            value="example3",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "Correspondence from DataSafe Campaign",
                    icon=green_icon
                ),
                dmc.AccordionPanel(
                    "Correspondence fro a think tank on their view on a recent policy announcement."
                ),
            ],
            value="example4",
        ),
    ],
)

])




##OVERALL LAYOUT
private_office_layout = html.Div(
    [
        dmc.Title("Box Busters", order=2),
        dmc.Tabs(
            [
                dmc.TabsList(
                    [   dmc.Tab(
                            "Upload", value = "upload"
                        ),
                        dmc.Tab(
                            "Box Processing",
                            value="tab_1",
                        ),
                        dmc.Tab(
                            "Ministerial View",
                            value="tab_2",
                        ),
                        dmc.Tab(
                            "Ministerial Returns",
                            value="tab_3",
                        ),
                        
                    ]
                ),
                dmc.TabsPanel( upload_page_layout, value = "upload"), 
                dmc.TabsPanel(private_office_box_processing_tab, value="tab_1"),
                dmc.TabsPanel(ministerial_view_layout, value="tab_2"),
                dmc.TabsPanel(ministerial_returns_layout, value="tab_3"),
            ],
            value="tab_1",
        ),
    ]
)






###PRIVATE OFFICE CALL BACKS
@app.callback(
    Output("pop-up-modal", "is_open"),
    [Input("open-pop-up", "n_clicks"), Input("close-pop-up", "n_clicks")],
    [State("pop-up-modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open



@app.callback(
    Output("summary-edited-version", "children"), Input("summary-edit-box", "value")
)
def update_output(value):
    return "{}".format(value)


@app.callback(
    Output("additional-content-edited-version", "children"), Input("additional-context-edit-box", "value")
)
def update_output(value):
    return "{}".format(value)



@app.callback(
       [ Output("saved-output-for-minister-summary","children")],Output("saved-output-for-ministerial-response-summary","children"), Input("close-pop-up", 'n_clicks'), State('summary-edit-box','value')
)
def update_output(n_clicks, summary):
   
    return  [html.Div(summary),html.Div(summary)]

@app.callback(
        [Output("saved-output-for-minister-context","children"),  Output("saved-output-for-ministerial-response-context","children")], Input("close-pop-up", 'n_clicks'), State('additional-context-edit-box','value')
)
def update_output(n_clicks, context):
   
    return  [html.Div(context), html.Div(context)]




##MINISTERIAL VIEW CALLBACKS



@app.callback(
    Output("pop-up-modal-minister", "is_open"),
    [Input("open-pop-up-minister", "n_clicks"), Input("close-pop-up-minister", "n_clicks")],
    [State("pop-up-modal-minister", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("pop-up-modal-ministerial-return", "is_open"),
    [Input("open-pop-up-ministerial-return", "n_clicks"), Input("close-pop-up-ministerial-return", "n_clicks")],
    [State("pop-up-modal-ministerial-return", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
        Output("ministerial_comments","children"), Input("close-pop-up-minister", 'n_clicks'), State('ministers-comments-input','value')
)
def update_comments(n_clicks, summary):
   
    return  html.Div(summary)


@app.callback(
    Output('icon_of_interest','children'), Input ('priority_dropdown', 'value')
)
def update_icon(selected):
    if selected == 'High':
        icon_view = red_icon
    elif selected == "Medium":
        icon_view = orange_icon
    elif selected == 'Low':
        icon_view = green_icon
    
    return icon_view