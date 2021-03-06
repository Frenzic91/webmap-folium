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

fgv = folium.FeatureGroup(name="Volcanoes")
for lat, lon, elev in zip(latitudes, longitudes, elevations):
    fgv.add_child(folium.CircleMarker(location=(lat, lon), tooltip=folium.Tooltip(html % elev), 
                 color=color_producer(elev), fill_color=color_producer(elev)))

fgp = folium.FeatureGroup(name="Populations")
data = open("world.json", "r", encoding="utf-8-sig").read()
fgp.add_child(folium.GeoJson(data, style_function=lambda x: {"fillColor":"green"
if x["properties"]["POP2005"] < 10000000 else "orange"
if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("webmap1.html")

