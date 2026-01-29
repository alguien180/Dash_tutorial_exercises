from dash import Dash, html, dcc
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







if __name__ =='__main__':
    app.run(debug=True)

