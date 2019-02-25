import folium
import pandas 

data = pandas.read_csv('Volcanoes.txt')
latitudes = list(data["LAT"])
longitudes = list(data["LON"])
elevations = list(data["ELEV"])

map = folium.Map(location=(38.58, -99.09), zoom_start=6)

fg = folium.FeatureGroup(name="MapLayer1")
for lat, lon, elev in zip(latitudes, longitudes, elevations):
    fg.add_child(folium.Marker(location=(lat, lon), popup=str(elev)+" m", icon=folium.Icon(color="red")))

map.add_child(fg)
map.save("webmap1.html")

