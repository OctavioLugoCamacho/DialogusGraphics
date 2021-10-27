import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = html.Div(
[
        dbc.Button("Primary", color="primary", className="me-1"),
        dbc.Button("Secondary", color="secondary", className="me-1"),
        dbc.Button("Success", color="success", className="me-1"),
        dbc.Button("Warning", color="warning", className="me-1"),
        dbc.Button("Danger", color="danger", className="me-1"),
        dbc.Button("Info", color="info", className="me-1"),
        dbc.Button("Light", color="light", className="me-1"),
        dbc.Button("Dark", color="dark", className="me-1"),
        dbc.Button("Link", color="link"),
        dbc.Alert("This is a primary alert", color="primary"),
        dbc.Row(dbc.Col(html.Div("A single column"))),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ]
        ),
        dbc.Nav(
            [
                dbc.NavLink("Internal link", href="/l/components/nav"),
                dbc.NavLink("External link", href="https://github.com"),
                dbc.NavLink(
                    "External relative",
                    href="/l/components/nav",
                    external_link=True,
                ),
                dbc.NavLink("Button", id="button-link", n_clicks=0),
            ]
        ),
        html.Br(),
        html.P(id="button-clicks"),
    ]
)

if __name__ == "__main__":
    app.run_server()

    