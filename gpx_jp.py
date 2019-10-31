import gpxpy
import gpxpy.gpx
import folium

print("start")

#gpxファイルの読み込み 
gpx_file = open('test.gpx', 'r')

gpx = gpxpy.parse(gpx_file)
points = []

for track in gpx.tracks:
	for segment in track.segments:
		for point in segment.points:
			points.append(tuple([point.latitude, point.longitude]))

#points表示する
#print(points)

ave_lat = sum(p[0] for p in points)/len(points)
ave_lon = sum(p[1] for p in points)/len(points)

my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=14)

#マップの種類追加
folium.TileLayer('Mapbox Bright').add_to(my_map)
folium.TileLayer('cartodbdark_matter').add_to(my_map)
folium.TileLayer('openstreetmap').add_to(my_map)
folium.LayerControl().add_to(my_map)

'''
#印をつける
for each in points:
	folium.Marker(each).add_to(my_map)
'''

#線を引く
folium.PolyLine(points, color="green", weight=2.5, opacity=1).add_to(my_map)

#保存 
my_map.save("test.html")

print("end")