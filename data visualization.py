import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Initialize the Dash app
app = dash.Dash(__name__)

# Sample dataset (you can replace this with your own dataset)
data = {
    'StudentID': list(range(1, 16)),
    'Maths': [85, 90, 78, 92, 88, 75, 80, 85, 92, 90, 70, 85, 88, 78, 82],
    'Science': [75, 82, 80, 88, 85, 90, 85, 88, 92, 80, 85, 82, 78, 85, 90],
    'History': [70, 75, 68, 80, 72, 78, 82, 75, 80, 85, 88, 82, 75, 80, 78]
}
df = pd.DataFrame(data)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Student Marks Visualization"),

    html.Div([
        dcc.Dropdown(
            id='subject',
            options=[{'label': col, 'value': col} for col in df.columns[1:]],
            value='Maths',
            clearable=False
        ),
        html.Label('Subject')
    ], style={'width': '48%', 'display': 'inline-block'}),

    dcc.Graph(id='bar-chart'),
])


# Callback to update the bar chart
@app.callback(
    Output('bar-chart', 'figure'),
    [Input('subject', 'value')]
)
def update_bar_chart(subject):
    fig = px.bar(df, x='StudentID', y=subject, title=f'{subject} Marks Distribution')
    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
