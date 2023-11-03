from dash import *
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


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
                            title='Громадянство людей')

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

gender_counts = df['gender'].value_counts()
pie_chart_gender = px.pie(names=gender_counts.index,
                          values=gender_counts.values, title='Гендер людей')

corr_matrix = df[['age', 'finalWorth', 'rank']].corr()

heatmap_age_worth_rank = go.Figure(data=go.Heatmap(z=corr_matrix.values,
                                                   x=corr_matrix.columns,
                                                   y=corr_matrix.columns,
                                                   colorscale='Viridis'))

heatmap_age_worth_rank.update_layout(title='Кореляція за віком, вартістю, рангом',
                                     xaxis_nticks=len(corr_matrix.columns),
                                     yaxis_nticks=len(corr_matrix.columns))

categories = df['category'].unique()

box_traces = []

for category in categories:
    # Filter the data for the current category
    category_data = df[df['category'] == category]['finalWorth']

    # Create a box trace for the current category
    box_trace = go.Box(y=category_data, name=category)

    # Add the box trace to the list
    box_traces.append(box_trace)

layout = go.Layout(title='Вартість людини та її галузь',
                   yaxis=dict(title='Final Worth'))

box_plot_worth_category = go.Figure(data=box_traces, layout=layout)

# Bar chart for Tax Revenue and Total Tax Rate
bar_tax_revenue_total_rate = px.bar(df, x='tax_revenue_country_country',
                                    y='total_tax_rate_country', title='Податкові надходження порівняно із загальною податковою ставкою')

# Scatter plot for CPI and GDP
scatter_cpi_gdp = px.scatter(
    df, x='cpi_country', y='gdp_country', title='ІСЦ до ВВП')

choropleth_map = px.choropleth(df,
                               locations='country',
                               locationmode='country names',
                               color='total_tax_rate_country',
                               color_continuous_scale='Viridis',
                               hover_name='country',
                               title='Рівень податків за країною')

# Customize map layout
choropleth_map.update_geos(fitbounds="locations", visible=False)
choropleth_map.update_layout(mapbox_style="carto-positron",
                             mapbox_zoom=1,
                             margin={"r": 0, "t": 0, "l": 0, "b": 0})


app.layout = html.Div([
    html.Div([
        dcc.Graph(figure=human_worth_age)
    ], style={'width': '33%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(figure=heatmap_age_worth_rank)
    ], style={'width': '33%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(figure=pie_chart_gender)
    ], style={'width': '33%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(figure=industries_graph)
    ], style={'width': '49%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(figure=box_plot_worth_category)
    ], style={'width': '49%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(figure=maps_humans),
    ], style={'width': '49%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(figure=bar_tax_revenue_total_rate),
    ], style={'width': '49%', 'display': 'inline-block'}),


    html.Div([
        dcc.Graph(figure=scatter_cpi_gdp)
    ], style={'width': '49%', 'display': 'inline-block'}),

    html.Div([
        dcc.Graph(figure=choropleth_map)
    ], style={'width': '49%', 'display': 'inline-block'}),

    # html.Div([ dcc.Graph(id='choropleth-map', figure=map_figure),
    #     dcc.Dropdown(id='variable-dropdown',
    #                  options=[{'label': var, 'value': var}
    #                           for var in map_options],
    #                  value=initial_variable)
    # ], style={'width': '49%', 'display': 'inline-block'}),

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
