import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go

# Load data from direct URLs to raw CSV files
data_url1 = '/Users/mridulsmac/Desktop/Dashboard/Placement Statistics-2023.csv'
df2023 = pd.read_csv(data_url1)
data_url2 = '/Users/mridulsmac/Desktop/Dashboard/Placement Statistics-2022.csv'
df2022 = pd.read_csv(data_url2)
data_url3 = '/Users/mridulsmac/Desktop/Dashboard/Placement Statistics-2021.csv'
df2021 = pd.read_csv(data_url3)
data_url4 = '/Users/mridulsmac/Desktop/Dashboard/Placement Statistics-2020.csv'
df2020 = pd.read_csv(data_url4)
data_url5 = '/Users/mridulsmac/Desktop/Dashboard/Placement Statistics-2019.csv'
df2019 = pd.read_csv(data_url5)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout
app.layout = dbc.Container(
    [
        html.Link(
            rel='stylesheet',
            href='/assets/styles.css'
        ),
        dbc.Navbar(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src="https://jssaten.ac.in//assets/images/logo/jsslogoicon.png", height="150px", width="150px"), className="ml-3"),
                            dbc.Col(html.H1("Placement Dashboard", className="ml-4", style={"font-size": "32px", "margin-top": "20px"})),
                        ],
                        align="center"
                    ),
                    href="/",
                ),
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Home", href="/", style={'color': 'white'}), className="ml-4", id="home-link"),
                        dbc.NavItem(dbc.NavLink("AvgGraph", href="/AvgGraph", style={'color': 'white'}), id="avg-link"),
                        dbc.NavItem(dbc.NavLink("2023", href="/year/2023", style={'color': 'white'}), id="year-2023-link"),
                        dbc.NavItem(dbc.NavLink("2022", href="/year/2022", style={'color': 'white'}), id="year-2022-link"),
                        dbc.NavItem(dbc.NavLink("2021", href="/year/2021", style={'color': 'white'}), id="year-2021-link"),
                        dbc.NavItem(dbc.NavLink("2020", href="/year/2020", style={'color': 'white'}), id="year-2020-link"),
                        dbc.NavItem(dbc.NavLink("2019", href="/year/2019", style={'color': 'white'}), id="year-2019-link"),
                    ],
                    className="ml-auto",
                    pills=True,
                    id="nav-links"
                ),
            ],
            color="dark",
            dark=True,
            id="navbar"
        ),
        dcc.Location(id='url', refresh=False, pathname='/'),
        html.Div(id='page-content'),
        html.Div("JSS Mahavidyapeeth", style={"text-align": "center", "padding": "100px"}),
    ],
)

# Callback to update page content based on the URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return generate_home_page_content()  # Call a function to generate content for the home page
    elif pathname == '/AvgGraph':        
        return generate_avg_salary_bar_graph()
    if pathname == '/year/2023':
        return generate_page_content(df2023, "Placement Statistics for 2023")
    elif pathname == '/year/2022':
        return generate_page_content(df2022, "Placement Statistics for 2022")
    elif pathname == '/year/2021':
        return generate_page_content(df2021, "Placement Statistics for 2021")
    elif pathname == '/year/2020':
        return generate_page_content(df2020, "Placement Statistics for 2020")
    elif pathname == '/year/2019':
        return generate_page_content(df2019, "Placement Statistics for 2019")

# Helper function to generate content for the home page
def generate_home_page_content():
    return html.Div([
        html.H2("Welcome to the Placement Dashboard"),
        html.P("This dashboard provides insights into the placement statistics of the institution."),
        html.P("Use the navigation bar to explore different sections."),
    ])

# Helper function to generate page content for a specific year
def generate_page_content(data_frame, title):
    # Sort the DataFrame by 'No. Of Offers' in descending order
    sorted_df = data_frame.sort_values(by='No. Of Offers', ascending=False)

    # Select the top 10 companies
    top_10_companies = sorted_df.head(10)

    return html.Div([
        html.H3(title),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H3("Companies Visited"),
                            html.H4(data_frame['Name of Company'].nunique())
                        ]),
                        color="primary",
                        style={'height': '100%'},
                    ),
                    width='3',
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H3("Highest (CTC)"),
                            html.H4(data_frame['CTC'].max())
                        ]),
                        color="primary",
                        style={'height': '100%'},
                    ),
                    width='3',
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H3("No. of Offers"),
                            html.H4(data_frame['No. Of Offers'].sum())
                        ]),
                        color="primary",
                        style={'height': '100%'},
                    ),
                    width='3',
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H3("Average (CTC)"),
                            html.H4(round(data_frame['CTC'].mean(), 2))
                        ]),
                        color="primary",
                        style={'height': '100%'},
                    ),
                    width='3',
                ),
            ],
            align="center",
            style={'height': '200px'},
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id='pie-chart',
                        figure=px.pie(top_10_companies, names='Name of Company', values='No. Of Offers', title='Pie Chart (Top 10 Recruiters)'),
                        style={'height': '500px', 'width': '800px'},
                        className='text-center'
                    ),
                ),
            ],
        ),
    ], style={'text-align': 'center'})

    
def generate_avg_salary_bar_graph():
        # Initialize lists to store average salary and years
        avg_salary_list = [6.76, 7.07, 5.05, 5.46, 4.2]
        year_list = [2023, 2022, 2021, 2020, 2019]

        # Create a bar graph
        fig = go.Figure()
        fig.add_trace(go.Bar(x=year_list, y=avg_salary_list, name='Average Salary', marker_color='royalblue'))
        fig.update_layout(title='Average Salary Over the Years', xaxis_title='Year', yaxis_title='Average Salary')
    
        return dcc.Graph(id='avg-salary-graph', figure=fig)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
