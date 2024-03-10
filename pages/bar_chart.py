from taipy.gui import Markdown
import pandas as pd

# read data
DATA = pd.read_csv("data.csv")

YEARS = list(DATA.columns[1:])
COUNTRIES = DATA["Country Name"].tolist()

#Default country --> Angola
selected_country = COUNTRIES[4]
COUNTRY_DATA1 = DATA[DATA["Country Name"] == selected_country].iloc[0, 1:]

def choose_country(state):
    COUNTRY_DATA1 = DATA[DATA["Country Name"] == state.selected_country].iloc[0, 1:]
    state.bar_chart = {
        "Year": list(DATA.columns[1:]),
        "CO2 Emission": list(COUNTRY_DATA1),
    }

bar_chart = {
    "Year": list(DATA.columns[1:]),
    "CO2 Emission": list(COUNTRY_DATA1),
}

# Creating Page
bar_chart_page = Markdown("bar_chart.md")
bar_chart_page.choose_country = choose_country
bar_chart_page.bar_chart = bar_chart



