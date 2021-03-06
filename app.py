# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from modules.basic_test_module.module import BasicTestModule as md

app = dash.Dash()

# Initize modules
module_one = md()

# Set the layout from the modules
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    # adds a view from one of the modules
    module_one.get_view()
    # dcc.Graph(
    #     id='example-graph',
    #     figure={
    #         'data': [
    #             {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
    #             {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
    #         ],
    #         'layout': {
    #
    #
    #             'title': 'Josiah\'s and Gana\'s Dash Data Visualization'
    #
    #         }
    #     }
    # )
])

if __name__ == '__main__':
    app.run_server(debug=True)