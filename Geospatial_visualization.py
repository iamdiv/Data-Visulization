import folium
import matplotlib.pyplot as plt
from IPython.display import HTML, display
#style = Stamen Terrain
#style = Stamen Toner
#style = Mapbox Bright
canada_map = folium.Map(location=[56.130,-106.35],zoom_start = 4,tiles = 'Stamen Terrain')
#add red marker to the otnterio
#create a feature group
onterio = folium.map.FeatureGroup()
#style the feature group
onterio.add_child(folium.CircleMarker(
    [51.25,-85.32],
    radus = 5,
    color = 'red',
    fill_color = 'red'
))
canada_map.add_child(onterio)
folium.Marker([51.25,-85.32],
popup = 'onterio').add_to(canada_map)
canada_map.save(outfile=r'D:\IBM Certification\dataVisualization\canada_map.html')
display(canada_map)
