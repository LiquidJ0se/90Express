import folium
import pandas

vol=pandas.read_csv('90xdatabase.txt')
name=list(vol['city'])
st=list(vol['state'])
ln=list(vol['log'])
lt=list(vol['lat'])

def vol_pings():
       return 'blue'

bis=pandas.read_csv('90xbisdatabase.txt')
c=list(bis['company'])
lat=list(bis['lat'])
log=list(bis['log'])
id=list(bis['id'])

def bis_pings(id):
   if id==1:
     return 'red'
   elif id==2:
     return 'orange'
   else: 
    return 'purple'

    
map=folium.Map(location=[41.4993,-81.6944],zoom_start=6,tiles='Stamen Terrain')

fg=folium.FeatureGroup(name='locations')
fg2=folium.FeatureGroup(name='Businesses')

for n,st,ln,lt in zip(name,st,ln,lt):
 fg.add_child(folium.Marker(location=[lt,ln],popup=str(n)+':'+str(st),fill_color=vol_pings(),color=vol_pings(),fill_opacity=0.7))

for c,lat,log,id in zip(c,lat,log,id):
 fg2.add_child(folium.CircleMarker(location=[lat,log],popup=str(c)+':'+str(),fill_color=bis_pings(id),color=bis_pings(id),fill_opacity=0.7))



map.add_child(fg)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save('90xMap1.html')
