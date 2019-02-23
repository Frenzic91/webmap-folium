import folium
import pandas 

data = pandas.read_csv('Volcanoes.txt')
latitudes = list(data["LAT"])
longitudes = list(data["LON"])

map = folium.Map(location=(38.58, -99.09), zoom_start=6)

fg = folium.FeatureGroup(name="MapLayer1")
for lat, lon in zip(latitudes, longitudes):
    fg.add_child(folium.Marker(location=(lat, lon), popup="I'm a random marker", icon=folium.Icon(color="red")))

map.add_child(fg)
map.save("webmap1.html")

