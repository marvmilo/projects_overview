import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
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
emoji_style = {
    "font-family": "apple color emoji,segoe ui emoji,noto color emoji,android emoji,emojisymbols,emojione mozilla,twemoji mozilla,segoe ui symbol"
}

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
                            html.H3(project["name"]),
                            dbc.Badge(project["status"], color = color),
                            html.Div(
                                html.H1(
                                    emoji.emojize(project["icon"]),
                                    style = {"font-size": "75px"}
                                ),
                                style = flex_style
                            ),
                            html.Br(),
                            html.Div(
                                html.A(
                                    dbc.Button(
                                        "VIEW",
                                        size = "lg",
                                        color = "primary",
                                        block = True
                                    ),
                                    href = project["url"],
                                    style = {"width": "200px"}
                                ),
                                style = flex_style
                            )
                        ],
                        color = "primary",
                        style = {
                            "height": "90%",
                            "width": "400px"
                        }
                    ),
                    html.Br(),
                ],
                width = "auto"
            )
        )
        
    #return row
    return dbc.Row(
        children = columns,
        justify = "center"
    )

#init app content
app.layout = html.Div(
    children = [
        #navbar for whole page
        dbc.NavbarSimple(
            children = [
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
                            )
                        ),
                        dbc.Col(
                            html.A(
                                dbc.Button(
                                    "Heroku",
                                    color = "primary",
                                    className = "ml-2"
                                ),
                                href = "https://dashboard.heroku.com/apps",
                                target = "_blank"
                            )
                        ),
                        dbc.Col(
                            html.A(
                                dbc.Button(
                                    "AWS",
                                    color = "primary",
                                    className = "ml-2"
                                ),
                                href = "https://aws.amazon.com/de/console/",
                                target = "_blank"
                            )
                        )
                    ],
                    no_gutters = True,
                    className="ml-auto flex-nowrap mt-3 mt-md-0"
                )
            ],
            brand = title,
            color = "primary",
            dark = True
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

#for debugging
if __name__ == '__main__':
    app.run_server(debug=True)