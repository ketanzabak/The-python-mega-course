import folium
import pandas
import json
import io

#read csv file
df = pandas.read_csv("data/Volcanoes-USA.txt")

#create map
map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=6)

'''
    Method used to select color based on attribute ELEV
'''
def color(elev):
    minimum = int(min(df['ELEV']))
    steps = int(max((df['ELEV']) - minimum )/3)
    if elev in range(minimum,minimum+steps):
        col = 'green'
    elif elev in range(minimum+steps , minimum+steps*2):
        col = 'blue'
    else:
        col = 'red'
    return col

feature_group = folium.FeatureGroup(name="Volcanoes-USA")

for lat,lon,name,lev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']) :
    #add simple marker
    feature_group.add_child(folium.Marker(location=[lat,lon],popup=name,icon = folium.Icon(color=color(lev))))

map.add_child(feature_group)
map.add_child(folium.GeoJson(data=open('data/world-geojson-from-ogr.json','r',encoding='utf-8-sig')),name='WorldPopulation')

#add layer control panel
map.add_child(folium.LayerControl())
#save map to file .
map.save("data/test.html")
