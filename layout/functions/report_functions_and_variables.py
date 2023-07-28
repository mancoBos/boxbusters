from dash import html
import dash_mantine_components as dmc
from dash_iconify import DashIconify

red_icon =DashIconify(
                    icon="ion:warning-outline",
                    color=dmc.theme.DEFAULT_COLORS["red"][8],
                    width=20,
                )

orange_icon=DashIconify(
                        icon="mingcute:to-do-line",
                        color=dmc.theme.DEFAULT_COLORS["orange"][8],
                        width=20,
                    )

green_icon=DashIconify(
                        icon="material-symbols:info-outline",
                        color=dmc.theme.DEFAULT_COLORS["green"][8],
                        width=20,
                    )

def scrolling_object(content):
    return html.Div(
        className="text-container",
        children=[content],
        style={
            "display": "inline-block",
            "overflow-y": "auto",
            "overflow-x": "auto",
        },
    )


def sticky_object(content):
    return (
        html.Div(
            className="figure-container",
            children=[content],
            style={
                "flex": "0 0 50%",
                "position": "sticky",
                "top": "0",
            },
        ),
    )


dhsc_green = "#00AD93"

dhsc_purple = "#512698"
