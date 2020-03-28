
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
import pandas as pd
import dash_table as dt
from plotly import graph_objs as go
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np
import dash_bootstrap_components as dbc
import plotly.express as px

#######################################################
app = dash.Dash()
#######################################################
app.title = "Dash Tutorial"
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
data_store = pd.read_excel("C:/Users/32638/Desktop/Python_Dash/yt_dash/global_superstore_2016.xlsx", sheet_name="Orders", parse_dates=True)
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
data_store['Sales']=data_store['Sales'].map('{:,.0f}'.format)
data_store['Profit']=data_store['Profit'].map('{:,.0f}'.format)
#######################################################
def create_card(title, content):
    card = dbc.Card(
        dbc.CardBody(
            [
                html.H4(title, className="card-title"),
                html.Br(),
                html.Br(),
                html.H2(content, className="card-subtitle"),
                html.Br(),
                html.Br(),
                ]
        ),
        color="info", inverse=True
    )
    return(card)
card3 = create_card("Number of Doctors on Platform", 50)
card2 = create_card("Number of Patients on Platform", 50)
card1 = create_card("Number of Hospitals on Platform", 50)

card4 = create_card("Number of Doctors on Platform", 50)
card5 = create_card("Number of Patients on Platform", 50)
card6 = create_card("Number of Hospitals on Platform", 50)


card7 = create_card("Number of Doctors on Platform", 50)
card8 = create_card("Number of Patients on Platform", 50)
card9 = create_card("Number of Hospitals on Platform", 50)

#######################################################
app.layout = html.Div([

    dcc.Tabs([
        dcc.Tab(label="Doctors", children=[
                html.Div([
                    html.Div([
                        html.H1(children='Corporate Finance Dashboard',
                                className='ten columns',
                                style={
                                'margin-top': 20,
                                'float': 'right',
                                'position': 'relative'

                                }),
                        html.Img(
                            src="https://upload.wikimedia.org/wikipedia/de/thumb/b/b0/Ebner_Stolz_Logo.svg/1200px-Ebner_Stolz_Logo.svg.png",
                            className='two columns',
                            style={
                                'height': '6%',
                                'width': '6%',
                                'float': 'right',
                                'position': 'relative',
                                'margin-top': 20,
                            },
                        ),
                      # html.Div(children='''
                      #       Dash: A web application framework for Python,
                      # ''', className="ten columns")
                    ], className= "row"
                    ),

                    html.Div(
                        [
                            html.Div(dbc.Row([dbc.Col(id='card1', children=[card1], md=4),
                                              dbc.Col(id='card2', children=[card2], md=4),
                                              dbc.Col(id='card3', children=[card3], md=4)]),
                                     style={"color": "black", 'margin-top': 20, 'margin-bottom': 20}, className="twelve columns"),

                         ], className="row"
                     ),


                    html.Div(
                        [
                            html.Div(
                                [
                                    html.P('Choose City:'),
                                    dcc.Dropdown(
                                        id='City',
                                        options=[{'label': k, 'value': k} for k in sorted(set(data_store["City"]))],
                                        value='All',
                                        multi=True
                                    ),
                                ],
                                className='six columns'
                            ),

                        ], className="row", style={'margin-top': ''}

                    ),

                    html.Div(
                        [
                        html.Div([
                            dcc.Graph(
                                id='example-graph-1'
                            )
                            ], className= 'six columns'
                            ),

                            html.Div([
                                 dcc.Graph(id='Segment',
                                figure=go.Figure(
                                data=[go.Pie(labels= data_store["Segment"],
                                values=data_store["Sales"])],
                                layout=go.Layout(
                                title='Segment')))
                            ], className= 'six columns'
                            )
                        ], className="row"
                    ),

                    html.Div(
                        [
                        html.Div([
                            dcc.Graph(
                                id='example-graph-2'
                            )
                            ], className= 'six columns'
                            ),

                            html.Div([html.Img(id='cur_plot', src='')],
                                     id='plot_div', className= 'six columns'
                            )
                        ], className="row"
                    ),


                    html.Div(
                        [
                            html.Div([
                                dt.DataTable(
                                    id='Table_1',
                                    columns=[{"name": i, "id": i} for i in data_store[["Customer ID", "Customer Name", "City",
                                    "Product ID", "Sales", "Quantity", "Profit"]]],
                                    data=data_store[["Customer ID", "Customer Name", "City",
                                    "Product ID", "Sales", "Quantity", "Profit"]].to_dict('records'),
                                    filter_action="native",
                                    fixed_rows={ 'headers': True, 'data': 0 },
                                    sort_action="native",
                                    sort_mode="multi",
                                    style_cell_conditional=[
                                            {'if': {'column_id': 'all'},
                                             'width': '5%'},
                                            # {'if': {'column_id': 'City'},
                                            #  'width': '10%'},
                                            # {'if': {'column_id': 'Customer Name'},
                                            #  'width': '10%'},
                                            # {'if': {'column_id': 'Profit'},
                                            #  'width': '10%'},
                                            # {'if': {'column_id': 'Sales'},
                                            #  'width': '10%'},
                                            # {'if': {'column_id': 'Product ID'},
                                            #  'width': '10%'},
                                        ],
                                    style_table={
                                        'maxHeight': '300px',
                                        #'overflowY': 'scroll',
                                        #'overflowX': 'scroll',
                                        "margin-top" : "500",


                                    }
                                )
                            ], className='twelve columns'
                            )

                        ], className="row"
                    ),



                ], className='ten columns offset-by-one')
        ], style={"backgroundColor":"silver"}),
        #########################################################################################
        dcc.Tab(label="Patients", children=[
            html.Div([
                html.Div([
                    html.H1(children='Corporate Finance Dashboard',
                            className='ten columns',
                            style={
                                'margin-top': 20,
                                'float': 'right',
                                'position': 'relative'

                            }),
                    html.Img(
                        src="https://upload.wikimedia.org/wikipedia/de/thumb/b/b0/Ebner_Stolz_Logo.svg/1200px-Ebner_Stolz_Logo.svg.png",
                        className='two columns',
                        style={
                            'height': '6%',
                            'width': '6%',
                            'float': 'right',
                            'position': 'relative',
                            'margin-top': 20,
                        },
                    ),
                    # html.Div(children='''
                    #       Dash: A web application framework for Python,
                    # ''', className="ten columns")
                ], className="row"
                ),
                    html.Div([
                        html.Div(dbc.Row([dbc.Col(id='card4', children=[card4], md=4), dbc.Col(id='card5', children=[card5], md=4),
                                    dbc.Col(id='card6', children=[card6], md=4)]), style={"color":"black",'margin-top': 20})

                    ], className="twelve columns")
            ], className='ten columns offset-by-one')

        ], style={"backgroundColor":"silver", "fontsize":"22"}),
        #########################################################################################
        dcc.Tab(label="Hospital", children=[
            html.Div([
                html.Div([
                    html.H1(children='Corporate Finance Dashboard',
                            className='ten columns',
                            style={
                                'margin-top': 20,
                                'float': 'right',
                                'position': 'relative'

                            }),
                    html.Img(
                        src="https://upload.wikimedia.org/wikipedia/de/thumb/b/b0/Ebner_Stolz_Logo.svg/1200px-Ebner_Stolz_Logo.svg.png",
                        className='two columns',
                        style={
                            'height': '6%',
                            'width': '6%',
                            'float': 'right',
                            'position': 'relative',
                            'margin-top': 20,
                        },
                    ),
                    # html.Div(children='''
                    #       Dash: A web application framework for Python,
                    # ''', className="ten columns")
                ], className="row"
                ),
                html.Div([
                    html.Div(dbc.Row(
                        [dbc.Col(id='card7', children=[card4], md=4), dbc.Col(id='card8', children=[card5], md=4),
                         dbc.Col(id='card9', children=[card6], md=4)]), style={"color": "black", 'margin-top': 20})

                ], className="twelve columns"),
                html.Div([
                    px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"])

                ])
            ], className='ten columns offset-by-one')

        ], style={"backgroundColor": "silver", "fontsize": "22"})

    ])
], style={"fontSize":"16"})
#####################################################
@app.callback(
    dash.dependencies.Output("example-graph-1", "figure"),
    [dash.dependencies.Input("City", "value")]
)
def update_output(selector):
    data = []
    for city in selector:
        a =  data_store[data_store["City"] == city]
        #profit = a["Profit"].sum(axis=0, skipna=True)
        data.append({"x": a["City"], "y":  a["Sales"], "type": "bar", "name": city})
    figure = {
        'data': data,
        'layout': {
            'title': 'Graph 1',
            "showgrid" : "False",
            'xaxis': dict(
                title='City',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=20,
                    color='#7f7f7f'

    )),
            'yaxis': dict(
                title='Sales',
                titlefont=dict(
                    family='Helvetica, monospace',
                    size=20,
                    color='#7f7f7f',
                    showgrid = False
                ))
        }
    }
    return figure

#######################################################
if __name__ == '__main__':
    app.run_server(debug=True)