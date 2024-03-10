<|toggle|theme|>
<|navbar|lov={[ ("/home", " Home"), ("/worldwide_emissions", " Worldwide CO2 Emission"), ("/compare_countries", " Compare Countries"), ("/pie_chart", "Emissions by Year"), ("/bar_chart", " Emission by Country"), ("/reduce_emissions", " Resources"), ("/dataset", "Explore Dataset"), ("/carbon_footprint", "Questionnaire")]}|>
<|container|

# Compare **Countries**{: .color-primary} CO2 Emission!

<|1 1|layout|

### Choose **1st**{: style="color: #7ED957"} Country!

<|{country1}|selector|lov={COUNTRIES}|dropdown|on_change=choose_country|>

### Choose **2nd**{: style="color: #7ED957"} Country!

<|{country2}|selector|lov={COUNTRIES}|dropdown|on_change=choose_country|>
|>
<br />

<|{LINE_GRAPH_DATA}|chart|type=lines|x=Years|y[1]=Country1|y[2]=Country2|line[1]=solid|line[2]=dashed|>

|>
