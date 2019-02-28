import folium
import pandas 

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif elevation >= 1000 and elevation < 3000:
        return "orange"
    else:
        return "red"

data = pandas.read_csv('Volcanoes.txt')
latitudes = list(data["LAT"])
longitudes = list(data["LON"])
elevations = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map(location=(38.58, -99.09), zoom_start=6)

fg = folium.FeatureGroup(name="MapLayer1")
for lat, lon, elev in zip(latitudes, longitudes, elevations):
    fg.add_child(folium.CircleMarker(location=(lat, lon), tooltip=folium.Tooltip(html % elev), 
                 color=color_producer(elev), fill_color=color_producer(elev)))

data = open("world.json", "r", encoding="utf-8-sig").read()
fg.add_child(folium.GeoJson(data))

map.add_child(fg)
map.save("webmap1.html")

