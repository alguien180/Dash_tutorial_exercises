from dash import Dash, html
import pandas as pd

app = Dash()

app.layout=html.Div(children="testing the app")

if __name__ =='__main__':
    app.run(debug=True)
