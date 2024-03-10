<|toggle|theme|>
<|navbar|lov={[ ("/home", " Home"), ("/worldwide_emissions", " Worldwide CO2 Emission"), ("/compare_countries", " Compare Countries"), ("/pie_chart", "Emissions by Year"), ("/bar_chart", " Emission by Country"), ("/reduce_emissions", " Resources"), ("/dataset", "Explore Dataset"), ("/carbon_footprint", "Questionnaire")]}|>
<|container|

# CO2 **Bar Chart**{: .color-primary} for Selected Country!

### Choose *Country*{: style="color: #7ED957"} to View Bar Chart:

<|{selected_country}|selector|lov={COUNTRIES}|dropdown|on_change=choose_country|>

<br />

<|{bar_chart}|chart|type=bar|x=Year|y=CO2 Emission|title=CO2 Emission Over Years|>

|>
