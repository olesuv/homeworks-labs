from dash import *
import pandas as pd
import plotly.express as px


# Dataset was downloaded from:
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

# Define the available options for choropleth map
map_options = ['cpi_country', 'cpi_change_country', 'gdp_country',
               'gross_tertiary_education_enrollment', 'gross_primary_education_enrollment_country',
               'life_expectancy_country', 'total_tax_rate_country_country']

# Create an initial choropleth map (using 'cpi_country' as default)
initial_variable = 'cpi_country'
map_figure = px.choropleth(locations=df['countryOfCitizenship'],
                           locationmode="country names",
                           color=df[initial_variable],
                           hover_name=df['countryOfCitizenship'],
                           color_continuous_scale="Viridis",
                           title='Графік країн по характеристиці: ')


app.layout = html.Div([
    html.Div([
        dcc.Graph(figure=human_worth_age)
    ], style={'width': '49%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(figure=industries_graph)
    ], style={'width': '49%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(figure=maps_humans),
    ], style={'width': '49%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(id='choropleth-map', figure=map_figure),
        dcc.Dropdown(id='variable-dropdown',
                     options=[{'label': var, 'value': var}
                              for var in map_options],
                     value=initial_variable)
    ], style={'width': '49%', 'display': 'inline-block'}),
])


@app.callback(
    Output('choropleth-map', 'figure'),
    [Input('variable-dropdown', 'value')]
)
def update_choropleth_map(selected_variable):
    updated_figure = px.choropleth(locations=df['countryOfCitizenship'],
                                   locationmode="country names",
                                   color=df[selected_variable],
                                   hover_name=df['countryOfCitizenship'],
                                   color_continuous_scale="Viridis",
                                   title=f'Choropleth Map of {selected_variable}')

    return updated_figure


if __name__ == "__main__":
    app.run(debug=True)
