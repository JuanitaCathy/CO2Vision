from taipy.gui import Markdown
import pandas as pd

# Read the data
DATA = pd.read_csv("./data2.csv")


# logik
worldwide_emissions = {
    "Years": list(DATA.columns[1:]),
    "Total CO2 Emission": DATA.iloc[0, 1:].tolist(),
}

# Creating Page
worldwide_emission_page = Markdown("worldwide_emissions.md")
worldwide_emission_page.worldwide_emissions = worldwide_emissions

