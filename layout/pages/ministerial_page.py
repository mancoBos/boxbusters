
# import dash
# from dash import html, dcc, Input, Output, State
# import dash_bootstrap_components as dbc
# import dash_mantine_components as dmc


# # from app import app




# import dash
# from dash import html, dcc, Input, Output, State
# import dash_bootstrap_components as dbc
# import dash_mantine_components as dmc

# import pandas as pd

# from layout.functions.prep_data import *
# from layout.pages.private_office_page import ministerial_returns_tab_summary, ministerial_returns_tab_context
# from layout.functions.report_functions_and_variables import *

# from app import app

# # test_file = pd.read_fwf('data/uploads/example_summary.txt')2
# test_file = "SofS approved a sprint on Unblocking GP Data for researchers. This will commence on Monday 31st of July with the first workshop in the sprint. The initial phase will comprise of 5 workshops, detailed below, to gather as much information about concerns, considerations, and ideas that different stakeholders have on this issue. "
# current_date = pd.to_datetime("27/08/23")
# word_image_path = 'data/word.png'


# def extract_processed_file(file):
#     formatted_text = process_word_to_correct_format(file)
#     summary_note = create_summary_note_function(formatted_text)
#     additional_context = additional_context_function(formatted_text)
#     [file_title, SRO_name, due_date] = extract_relevant_info(formatted_text)
#     return [
#         formatted_text,
#         summary_note,
#         additional_context,
#         file_title,
#         SRO_name,
#         due_date,
#     ]


# def pop_up_review_box_minister(file):
#     [
#         formatted_text,
#         summary_note,
#         additional_context,
#         file_title,
#         SRO_name,
#         due_date,
#     ] = extract_processed_file(file)
#     return [   dbc.Row(
#                             [
#                                 dbc.Col([html.Div("SRO: " + SRO_name)]),
#                                 dbc.Col([html.Div("Due: " + due_date)]),
#                                 dbc.Col([html.Div("Download: "),html.Img(src=word_image_path)])
#                             ]
#                         ),              
#                                          html.Br(),
#         html.Div("Summary: "),
#         html.Div(ministerial_returns_tab_summary),
#         html.Br(),
#         html.Div("Additional Context: "),
#         # html.Div(edited_context_note),
#                                         dbc.Button(
#                                             "Save and Submit",
#                                             id="close-pop-up-minister",
#                                             className="ms-auto",
#                                             n_clicks=0,
#                                         ),
#                                     ]


# def item_box_minister(file):
#     [
#         formatted_text,
#         summary_note,
#         additional_context,
#         file_title,
#         SRO_name,
#         due_date,
#     ] = extract_processed_file(file)

#     return dmc.AccordionItem(
#         [
#             dmc.AccordionControl(
#                 file_title,
#                 icon=red_icon
#             ),
#             dmc.AccordionPanel(
#                 html.Div(
#                     [
#                         dbc.Row(
#                             [
#                                 dbc.Col([html.Div("SRO: " + SRO_name)]),
#                                 dbc.Col([html.Div("Due: " + due_date)]),
#                             ]
#                         ),
#                         html.Br(),
#                         ministerial_returns_tab_summary,
#                         html.Br(),
#                         html.Br(),
#                         dbc.Button("Review", id="open-pop-up-minister", n_clicks=0),
#                         dbc.Modal(
#                             [
#                                 dbc.ModalHeader(dbc.ModalTitle(file_title)),
#                                 dbc.ModalBody(pop_up_review_box_minister(file)
#                                 ),
#                             ],
#                             id="pop-up-modal-minister",
#                             size="xl",
#                             style={"max-width": "none", "height": "90%"},
#                             is_open=False,
#                         ),
#                     ]
#                 )
#             ),
#         ],
#         value="customization",
#     )


# final_box_view = dmc.Accordion(
#     children=[
#         item_box_minister(test_file),
#         dmc.AccordionItem(
#             [
#                 dmc.AccordionControl(
#                     "Correspondence from Ben Norman, Deputy Chief Fire",
#                     icon=orange_icon
#                 ),
#                 dmc.AccordionPanel(
#                     "The world is on fire!"
#                 ),
#             ],
#             value="example1",
#         ),
#         dmc.AccordionItem(
#             [
#                 dmc.AccordionControl(
#                     "For Info: Upcoming Departmental Hackathon",
#                     icon=green_icon
#                 ),
#                 dmc.AccordionPanel(
#                     "We are running a series of hackathons in the department to help find innovative tech solutions for pressing issues"
#                 ),
#             ],
#             value="example2",
#         ),
#         dmc.AccordionItem(
#             [
#                 dmc.AccordionControl(
#                     "For info: Updated National Recommendations on JARM Applications",
#                     icon=green_icon
#                 ),
#                 dmc.AccordionPanel(
# "Some new national guidelines you may be interested in!"                ),
#             ],
#             value="example3",
#         ),
#         dmc.AccordionItem(
#             [
#                 dmc.AccordionControl(
#                     "Correspondence from DataSafe campaign",
#                     icon=green_icon
#                 ),
#                 dmc.AccordionPanel(
#                     "Correspondence fro a think tank on their view on a recent policy announcement."
#                 ),
#             ],
#             value="example4",
#         ),
#     ],
# )

# ministerial_view_layout = html.Div(
#     [
#         html.Br(),
#         dmc.Title("Ministerial Box", order=2),
#         html.Br(),
#         final_box_view, ministerial_returns_tab_summary
#     ]
# )





# @app.callback(
#     Output("pop-up-modal-minister", "is_open"),
#     [Input("open-pop-up-minister", "n_clicks"), Input("close-pop-up-minister", "n_clicks")],
#     [State("pop-up-modal-minister", "is_open")],
# )
# def toggle_modal(n1, n2, is_open):
#     if n1 or n2:
#         return not is_open
#     return is_open

# # @app.callback(
# #         Output("saved-output-for-minister-delete","children"), Input("close-pop-up-minister", 'n_clicks'), State('summary-edit-box-minister','value'), State('additional-context-edit-box-minister','value')
# # )
# # def update_output(n_clicks, summary, context):
   
# #     layout =  html.Div([
# #         html.Br(),
# #         html.Div("Summary: "),
# #         html.Div(summary),
# #         html.Br(),
# #         html.Div("Additional Context: "),
# #         html.Div(context),
        
# #     ])
# #     return layout

# # @app.callback(
# #     Output("summary-edited-version-minister", "children"), Input("summary-edit-box-minister", "value")
# # )
# # def update_output(value):
# #     return "{}".format(value)


# # @app.callback(
# #     Output("additional-content-edited-version", "children"), Input("additional-context-edit-box", "value")
# # )
# # def update_output(value):
# #     return "{}".format(value)
