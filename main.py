from taipy.gui import Gui
from taipy import Core
from pages.home import home_page
from pages.bar_chart import bar_chart_page
from pages.compare_countries import compare_countries_page
from pages.worldwide_emissions import worldwide_emission_page
from pages.pie_chart import pie_chart_page
from pages.reduce_emissions import reduce_emission_page
from pages.dataset import dataset_page
from pages.carbon_footprint import carbon_footprint_page

stylekit = {
    "font-family": "Dancing Script"
    }

# Configuring Routes
ROUTES = {
    'home': home_page,
    'bar_chart': bar_chart_page,
    'worldwide_emissions': worldwide_emission_page,
    'pie_chart': pie_chart_page,
    'compare_countries': compare_countries_page,
    'reduce_emissions': reduce_emission_page,
    'dataset': dataset_page,
    'carbon_footprint': carbon_footprint_page
}

# Running Application 
if __name__ == '__main__':
    Core().run()
    app = Gui()
    app.add_pages(ROUTES)
    app.run(title="CO2Vision", watermark="CO2Vision", favicon="images/cropped-CO2 VISION 1.png", stylekit=stylekit)
