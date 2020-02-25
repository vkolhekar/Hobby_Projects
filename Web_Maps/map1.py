import folium
import os

flight_path = os.path.join('patni_ground.json')
map = folium.Map(location = [19.1786884,72.9900004], zoom_start = 17)
folium.GeoJson(flight_path, name = 'Flight Path').add_to(map)
map.save("cg_ground.html")