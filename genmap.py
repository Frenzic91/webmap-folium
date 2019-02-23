import folium
map = folium.Map(location=(38.58, -99.09), zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="MapLayer1")
fg.add_child(folium.Marker(location=(38.2, -99.1), popup="I'm a random marker", icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("webmap1.html")

