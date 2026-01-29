from dash import Dash, html, callback, Output, Input, dcc
import pandas as pd
import dash_ag_grid as dag
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app = Dash()

app.layout= [
    html.Div(children="testing the app"),
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{"field":i} for i in df.columns]
    ),
    dcc.Graph(figure=px.histogram(df,x='continent',y='lifeExp',histfunc='avg'))
]
@callback(
    Output(component_id='controls-and-graph',component_property='figure'),
    Input(component_id='controls-and-radio-item',component_propery='value')

)
def update_graph(col_chosen):
    fig= px.histogram(df,x='continent',y=col_chosen,histfunc='avg')
    return fig





if __name__ =='__main__':
    app.run(debug=True)

