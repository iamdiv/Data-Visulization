import pandas as pd
import folium
from IPython.display import HTML, display
path = r"D:\IBM Certification\dataVisualization\Canada.xlsx"
geojson_file = r"D:\IBM Certification\dataVisualization\world_countries.json"
df_can  = pd.read_excel(path,sheet_name='Canada by Citizenship',
                    skiprows=range(20),
                    skipfooter=2)
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis = 1, inplace = True)
df_can.rename (columns = {'OdName':'Country', 'AreaName':'Continent','RegName':'Region'}, inplace = True)
df_can.columns = list(map(str, df_can.columns))

#df_can.set_index('Country', inplace = True)

df_can['Total'] =  df_can.sum (axis = 1)
world_map = folium.Map(location = [0,0],zoom_start = 2,tiles = 'Mapbox Bright')

print(df_can.head())
# generate choropleth map using the total immigration of each country to Canada from 1980 to 2013
world_map.choropleth(
    geo_data = geojson_file,
    data = df_can,
    columns = ['Country', 'Total'],
    key_on='feature.properties.name',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Immigration to Canada'
)

world_map.save(outfile=r'D:\IBM Certification\dataVisualization\world_map.html')
display(world_map)