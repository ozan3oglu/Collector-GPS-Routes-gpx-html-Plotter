# python .\Gpxcomp.py IMEI START_TIME END_TIME ARG1 ARG2
# python .\Gpxcomp.py 862096048032002 2022-08-24-12:29:56 2022-08-24-12:51:37 -g -k         Dual .gpx
# python .\Gpxcomp.py 862096048032002 2022-08-24-12:29:56 2022-08-24-12:51:37 -k            Kalman .gpx
# python .\Gpxcomp.py 862096048032002 2022-08-24-12:29:56 2022-08-24-12:51:37 -g            Collector .gpx

from fileinput import filename
import sys
import gpxpy
import gmplot   # (https://github.com/vgm64/gmplot)
import pandas as pd
import folium 
import os
import webbrowser
import argparse


imei = sys.argv[1]
start = sys.argv[2]
end = sys.argv[3]

try:
    process = sys.argv[4] if len(sys.argv[4]) >= 1 else None
except:
    process = "Collector not in args."
    pass    
try:
    process1 = sys.argv[5] if len(sys.argv[5]) >= 1 else  None
except:
    process1 = "Kalman not in args."
    pass

def GPS_draw_double():
    gpxFileName = "%s_%s_%s_notfiltered.gpx" % (imei, start.replace(":", "-"), end.replace(":", "-"))
    print(gpxFileName)
    gpxFileName1 = "%s_%s_%s_kalman.gpx" % (imei, start.replace(":", "-"), end.replace(":", "-"))

    gpx = gpxpy.parse(open(gpxFileName))

    # Files can have more than one track, which can have more than one segment, which have more than one point...
    print('Num tracks: ' + str(len(gpx.tracks)))
    track = gpx.tracks[0]
    print('Num segments: ' + str(len(track.segments)))
    segment = track.segments[0]
    print('Num segments: ' + str(len(segment.points)))

    # Load the data into a Pandas dataframe (by way of a list)
    data = []
    segment_length = segment.length_3d()
    for point_idx, point in enumerate(segment.points):
        data.append([point.longitude, point.latitude,point.elevation,
                    point.time, segment.get_speed(point_idx)])

    columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
    df = pd.DataFrame(data, columns=columns)
    print('\nDataframe head:')
    print(df)
    print('\nNum non-None Longitude records: ' + str(len(df[~pd.isnull(df.Longitude)])))
    print('Num non-None Latitude records: ' + str(len(df[~pd.isnull(df.Latitude)])))
    print('Num non-None Altitude records: ' + str(len(df[~pd.isnull(df.Altitude)])))
    print('Num non-None Time records: ' + str(len(df[~pd.isnull(df.Time)])))
    print('Num non-None Speed records: ' + str(len(df[~pd.isnull(df.Speed)])))

    mymap = folium.Map( location=[ df.Latitude.mean(), df.Longitude.mean() ], zoom_start=14)
    folium.PolyLine(df[['Latitude','Longitude']].values, color="red", weight=2.5, opacity=1).add_to(mymap)
    
    #Kalman filtered below.

    gpx = gpxpy.parse(open(gpxFileName1))

    
    print('Num tracks: ' + str(len(gpx.tracks)))
    track = gpx.tracks[0]
    print('Num segments: ' + str(len(track.segments)))
    segment = track.segments[0]
    print('Num segments: ' + str(len(segment.points)))

    # Load the data into a Pandas dataframe (by way of a list)
    data = []
    segment_length = segment.length_3d()
    for point_idx, point in enumerate(segment.points):
        data.append([point.longitude, point.latitude,point.elevation,
                    point.time, segment.get_speed(point_idx)])

    columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
    df = pd.DataFrame(data, columns=columns)
    print('\nDataframe head:')
    print(df)
    print('\nNum non-None Longitude records: ' + str(len(df[~pd.isnull(df.Longitude)])))
    print('Num non-None Latitude records: ' + str(len(df[~pd.isnull(df.Latitude)])))
    print('Num non-None Altitude records: ' + str(len(df[~pd.isnull(df.Altitude)])))
    print('Num non-None Time records: ' + str(len(df[~pd.isnull(df.Time)])))
    print('Num non-None Speed records: ' + str(len(df[~pd.isnull(df.Speed)])))

    mymap1 = folium.Map( location=[ df.Latitude.mean(), df.Longitude.mean() ], zoom_start=14)
    folium.PolyLine(df[['Latitude','Longitude']].values, color="blue", weight=2.5, opacity=1).add_to(mymap)

    #Combining two gpx file.
    mymap.add_child(mymap1)
    mymap.save( "%s_%s_%s_dual.html" % (imei, start.replace(":", "-"), end.replace(":", "-")))

    htmlFileName = "%s_%s_%s_dual.html" % (imei, start.replace(":", "-"), end.replace(":", "-"))
    webbrowser.open_new_tab(htmlFileName)

def GPS_draw(draw,linecolor,gpxdata):

    gpxFileName = "%s_%s_%s%s.gpx" % (imei, start.replace(":", "-"), end.replace(":", "-"),draw)
    print(gpxFileName)

    gpx = gpxpy.parse(open(gpxFileName))

    # Files can have more than one track, which can have more than one segment, which have more than one point...
    print('Num tracks: ' + str(len(gpx.tracks)))
    track = gpx.tracks[0]
    print('Num segments: ' + str(len(track.segments)))
    segment = track.segments[0]
    print('Num segments: ' + str(len(segment.points)))

    # Load the data into a Pandas dataframe (by way of a list)
    data = []
    segment_length = segment.length_3d()
    for point_idx, point in enumerate(segment.points):
        data.append([point.longitude, point.latitude,point.elevation,
                    point.time, segment.get_speed(point_idx)])

    columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
    df = pd.DataFrame(data, columns=columns)
    print('\nDataframe head:')
    print(df)
    print('\nNum non-None Longitude records: ' + str(len(df[~pd.isnull(df.Longitude)])))
    print('Num non-None Latitude records: ' + str(len(df[~pd.isnull(df.Latitude)])))
    print('Num non-None Altitude records: ' + str(len(df[~pd.isnull(df.Altitude)])))
    print('Num non-None Time records: ' + str(len(df[~pd.isnull(df.Time)])))
    print('Num non-None Speed records: ' + str(len(df[~pd.isnull(df.Speed)])))

    mymap = folium.Map( location=[ df.Latitude.mean(), df.Longitude.mean() ], zoom_start=14)
    folium.PolyLine(df[['Latitude','Longitude']].values, color=linecolor, weight=2.5, opacity=1).add_to(mymap)
    #mymap   # shows map inline in Jupyter but takes up full width

    mymap.save( "%s_%s_%s_%s.html" % (imei, start.replace(":", "-"), end.replace(":", "-"),gpxdata))

    htmlFileName = "%s_%s_%s_%s.html" % (imei, start.replace(":", "-"), end.replace(":", "-"),gpxdata)
    webbrowser.open_new_tab(htmlFileName)

    
def main() :

    command = ""
    command1 = ""

    print("IMEI : ",imei)
    print("START TIME : ",start)
    print("END TIME : ",end)

    if (process == "-g" and process1 != "-k"):      
        command = 'python .\collector\collector-parser.py -s ' + imei + ' ' + start + ' ' + end + ' ' + process
        os.system(command)
        print("Collector has worked!")
        draw = "_notfiltered"
        linecolor = "red"
        gpxdata="notfiltered"
        GPS_draw(draw,linecolor,gpxdata)
        

    elif (process == "-k" and process1 != "-g") :
        command1 =  'python .\collector_kalman_filter\collector-parser.py -s ' + imei + ' ' + start + ' ' + end + ' ' + process 
        os.system(command1) 
        print("Kalman Filter has worked!")
        draw = "_kalman"
        linecolor ="blue"
        gpxdata = "kalman"
        GPS_draw(draw,linecolor,gpxdata)

    elif (process == "-g" and process1 == "-k") or (process == "-k" and process1 == "-g"):
        command = 'python .\collector\collector-parser.py -s ' + imei + ' ' + start + ' ' + end + ' ' + process
        os.system(command)
        command1 =  'python .\collector_kalman_filter\collector-parser.py -s ' + imei + ' ' + start + ' ' + end + ' ' + process1 
        os.system(command1)
        GPS_draw_double()
    
main()


