from dash import *
import pandas as pd
import plotly.express as px


# Dataset was downloasded from:
# https://www.kaggle.com/datasets/nelgiriyewithana/billionaires-statistics-dataset/
df = pd.read_csv('BillionairesStatisticsDataset.csv')

app = Dash(__name__)

# Scatter plot
human_worth_age = px.scatter(df, x='age', y='finalWorth',
                             title='Вартість людини та її вік',
                             hover_data='personName')

# Pie chart
industry_counts = df['industries'].value_counts()
industries_graph = px.pie(names=industry_counts.index, values=industry_counts.values,
                   title='Галузі заробітку')

# Choropleth map for countryOfCitizenship
humans_countries = df['countryOfCitizenship'].value_counts()
maps_humans = px.choropleth(locations=humans_countries.index, locationmode="country names", color=humans_countries.values,
                            hover_name=humans_countries.index, color_continuous_scale="Viridis",
                            title='Кількість людей за громадянством')

app.layout = html.Div([
    html.Div([
        dcc.Graph(figure=human_worth_age)
    ], style={'width': '49%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(figure=industries_graph)
    ], style={'width': '49%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(figure=maps_humans)
    ])
])


if __name__ == "__main__":
    app.run(debug=True)
