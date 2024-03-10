<|toggle|theme|>
<|navbar|lov={[ ("/home", " Home"), ("/worldwide_emissions", " Worldwide CO2 Emission"), ("/compare_countries", " Compare Countries"), ("/pie_chart", "Emissions by Year"), ("/bar_chart", " Emission by Country"), ("/reduce_emissions", " Resources"), ("/dataset", "Explore Dataset"), ("/carbon_footprint", "Questionnaire")]}|>
<|container|

# CO2 **Pie Chart**{: .color-primary} for Selected Country!

### Choose *Country*{: style="color: #7ED957"} to View Pie Chart:

<|{selected_country}|selector|lov={COUNTRIES}|dropdown|on_change=choose_country|>

<br />

<|{pie_chart}|chart|type=pie|labels=Year|values=CO2 Emission|options={pie_options}|title=CO2 Emission Over Years|>

|>
