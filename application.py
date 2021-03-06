import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import json
import emoji

#app values
title = "Projects Overview"
external_stylesheets = [dbc.themes.BOOTSTRAP]
meta_tags = [{"name": "viewport", "content": "width=device-width, initial-scale=1"}]

#html values
flex_style = {
    "display": "flex",
    "justify-content": "center",
    "align-items": "center"
}
navbar_spacing = html.Div(style = {"width": "5px"})

#init app
app = dash.Dash( 
    external_stylesheets=external_stylesheets,
    meta_tags=meta_tags,
    suppress_callback_exceptions=True
)
app.title = title
server = app.server

#function for creating page content
def page_content():
    projects = json.loads(open("projects.json").read())
    columns = []
    
    #iter over pojects
    for project in projects:
        
        #set color of badge
        if project["status"] == "ONLINE":
            color = "success"
        elif project["status"] == "OFFLINE":
            color = "danger"
        else:
            color = "warning"
        
        #create project cards
        columns.append(
            dbc.Col(
                children = [
                    dbc.Alert(
                        children = [
                            html.H4(project["name"]),
                            dbc.Badge(project["status"], color = color),
                            html.Div(
                                html.H1(
                                    emoji.emojize(project["icon"]),
                                    style = {"font-size": "50px"}
                                ),
                                style = flex_style
                            ),
                            html.Br(),
                            html.Div(
                                html.A(
                                    dbc.Button(
                                        "VIEW",
                                        color = "primary",
                                        block = True
                                    ),
                                    href = project["url"],
                                    target = "_blank",
                                    style = {"width": "200px"}
                                ),
                                style = flex_style
                            ),
                            html.Div(style = {"width": "300px"})
                        ],
                        color = "primary",
                        style = {
                            "height": "90%"
                        }
                    ),
                    html.Br(),
                ]
            )
        )
        
    #return row
    return dbc.Row(
        children = columns
    )

#init app content
app.layout = html.Div(
    children = [
        #navbar
        
        #Navbar
        dbc.Navbar(
            children = [
                #navbar title
                dbc.Row(
                    children = [
                        dbc.Col(
                            " ".join(word.upper()),
                            style = {
                                "font-size": "20px",
                                "color": "white",
                                "white-space": "nowrap"
                            },
                            width = "auto"
                        )
                        for word in title.split(" ")
                    ],
                    style = {
                        "width": "300px",
                        "max-width": "85%"
                    }
                ),
        
                #navbar toggler
                dbc.NavbarToggler(id = "nav-toggler"),
                
                #navbar interactions
                dbc.Collapse(
                    dbc.Row(
                        children = [
                            dbc.Col(
                                html.A(
                                    dbc.Button(
                                        "Github",
                                        color = "primary",
                                        className = "ml-2"
                                    ),
                                    href = "https://github.com/marvmilo?tab=repositories",
                                    target = "_blank"
                                ),
                                width = "auto"
                            ),
                            navbar_spacing,
                            dbc.Col(
                                html.A(
                                    dbc.Button(
                                        "Heroku",
                                        color = "primary",
                                        className = "ml-2"
                                    ),
                                    href = "https://dashboard.heroku.com/apps",
                                    target = "_blank"
                                ),
                                width = "auto"
                            ),
                            navbar_spacing,
                            dbc.Col(
                                html.A(
                                    dbc.Button(
                                        "AWS",
                                        color = "primary",
                                        className = "ml-2"
                                    ),
                                    href = "https://aws.amazon.com/de/console/",
                                    target = "_blank"
                                ),
                                width = "auto"
                            )
                        ],
                        justify = "end",
                        no_gutters = True,
                        style = {"width": "100%"}
                    ),
                    navbar = True,
                    id = "nav-collapse"
                )
            ],
            color = "primary",
            dark = True,
            style = {"padding": "20px 40px"}
        ),
        
        #page content
        html.Div(
            page_content(),
            style = {
                "padding": "5%",
                "font-family": "apple color emoji,segoe ui emoji,noto color emoji,android emoji,emojisymbols,emojione mozilla,twemoji mozilla,segoe ui symbol"
            }
        )
    ]
)

#navbar collapse callback
@app.callback(
    [Output("nav-collapse", "is_open")],
    [Input("nav-toggler", "n_clicks")],
    [State("nav-collapse", "is_open")]
)
def toggle_navbar_collapse(n_clicks, is_open):
    if n_clicks:
        return [not is_open]
    return [is_open]

#for debugging
if __name__ == '__main__':
    app.run_server(debug=True)