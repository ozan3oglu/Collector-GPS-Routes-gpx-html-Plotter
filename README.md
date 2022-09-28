# Route-Collector-Plot-GPX

  Converting GPS data to gpx format in csv and plotting routes for comparison after filter applied

  GPS data obtained from the device is collected with the help of Collector. The data obtained after entering the IMEI and time range is written to a cvs file. Kalman Filter is applied for GPS route correction over this data and written to a csv file. By converting these csv files to Gpx files, both routes can be followed in a new tab in the browser.

  *** In the name of the confidentiality of the studies, the information of the collector and collector_kalman_filter software, from which the data were  obtained, is hidden. For this purpose, the relevant code part and .py files are hidden.
  
  
# python .\Gpxcomp.py IMEI START_TIME END_TIME ARG1 ARG2

Arguments

ARG1 = {-g,-k}
ARG2 = {-k}

Routes about arguments

-g -k         Dual .gpx   ------> Two routes plotted at the same time
-k            Kalman .gpx   ------> Kalman filtered route plotted
-g            Collector .gpx   ------> Collector data route plotted
