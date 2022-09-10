# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                
                                dcc.Dropdown(id='site-dropdown',
                                            options=[
                                               {'label': 'All Sites', 'value': 'ALL'},
                                               {'label': 'CCAFS LC-40', 'value': 'site1'},
                                               {'label': 'VAFB SLC-4E', 'value': 'site2'},
                                               {'label': 'KSC LC-39A', 'value': 'site3'},
                                               {'label': 'CCAFS SLC-40', 'value': 'site4'},
                                                     ],
                                            value='ALL',
                                            placeholder="Select a Launch Site here",
                                            searchable=True
                                        ),

                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site