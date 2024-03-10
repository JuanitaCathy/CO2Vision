import pandas as pd
from taipy.gui import Markdown

# read data
DATA = pd.read_csv("data.csv")

YEARS = list(DATA.columns[1:])
COUNTRIES = DATA["Country Name"].tolist()

#Default country --> Angola
selected_country = COUNTRIES[4]
COUNTRY_DATA1 = DATA[DATA["Country Name"] == selected_country].iloc[0, 1:]

def choose_country(state):
    COUNTRY_DATA1 = DATA[DATA["Country Name"] == state.selected_country].iloc[0, 1:]
    state.pie_chart = {
        "Year": list(DATA.columns[1:]),
        "CO2 Emission": list(COUNTRY_DATA1),
    }

pie_chart = {
    "Year": list(DATA.columns[1:]),
    "CO2 Emission": list(COUNTRY_DATA1),
}

pie_options = {
    "textinfo": "none"
}

# Creating Page
pie_chart_page = Markdown("pie_chart.md")
pie_chart_page.choose_country = choose_country
pie_chart_page.pie_chart = pie_chart
