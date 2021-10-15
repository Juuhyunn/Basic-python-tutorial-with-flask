import pandas as pd
import folium

if __name__ == '__main__':
    url = (
        "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
    )
    state_geo = f"{url}/us-states.json"
    state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
    state_data = pd.read_csv(state_unemployment)

    # m = folium.Map(location=[37.50, 127], zoom_start=12)
    m = folium.Map(location=[37.5056, 127.12], zoom_start=20)

    folium.Choropleth(
        geo_data=state_geo,
        name="choropleth",
        data=state_data,
        columns=["State", "Unemployment"],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Unemployment Rate (%)",
    ).add_to(m)

    folium.LayerControl().add_to(m)

    m.save("./data/folium.html")

import csv
if __name__ == '__main__':
    crime_titles = ['살인', '강도', '강간', '절도', '폭력']
    crime_values = ['살인 발생', '강도 발생', '강간 발생', '절도 발생', '폭력 발생']  # Nominal
    dt = dict(zip(crime_titles, crime_values))
    print(dt)

    with open('./data/test.csv', 'w', encoding='UTF-8') as f:
        w = csv.writer(f)
        w.writerow(dt.keys())
        w.writerow(dt.values())