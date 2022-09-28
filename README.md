### Route-Collector-Plot-GPX

  Converting GPS data to gpx format in csv and plotting routes for comparison after filter applied

  GPS data obtained from the device is collected with the help of Collector. The data obtained after entering the IMEI and time range is written to a cvs file. Kalman Filter is applied for GPS route correction over this data and written to a csv file. These csv files are converted to Gpx files and an html file is created, and both routes can be followed in a new tab that opens automatically in the browser.

  *** In the name of the confidentiality of the studies, the information of the collector and collector_kalman_filter software, from which the data were  obtained, is hidden. For this purpose, the relevant code part and .py files are hidden.
  

## Terminal Commands

python .\Gpxcomp.py IMEI START_TIME END_TIME ARG1 ARG2

# Arguments

ARG1 = {-g,-k} \
ARG2 = {-k} 

# Routes with respect to arguments

-g -k         Dual .gpx   ------> Two routes plotted at the same time \
-k            Kalman .gpx   ------> Kalman filtered route plotted \
-g            Collector .gpx   ------> Collector data route plotted 


python .\Gpxcomp.py IMEI START_TIME END_TIME ARG1 ARG2

python .\Gpxcomp.py 862096048032002 2022-08-24-12:29:56 2022-08-24-12:51:37 -g -k  

![862096048032002_2022-08-24-12-29-56_2022-08-24-12-51-37_kalman](https://user-images.githubusercontent.com/110588407/192779782-c9e7543e-5758-4232-99c1-248abc035978.png)

![862096048032002_2022-08-24-12-29-56_2022-08-24-12-51-37_dual](https://user-images.githubusercontent.com/110588407/192779778-dce1a3fd-943d-47be-a9bf-d699e224d02f.png)


python .\Gpxcomp.py 862096048032002 2022-08-24-12:29:56 2022-08-24-12:51:37 -k         

![Screenshot_1](https://user-images.githubusercontent.com/110588407/192781160-340e329a-53b5-45d1-b43a-91cc126695f5.png)



python .\Gpxcomp.py 862096048032002 2022-08-24-12:29:56 2022-08-24-12:51:37 -g      

![862096048032002_2022-08-24-12-29-56_2022-08-24-12-51-37_notfiltered](https://user-images.githubusercontent.com/110588407/192779767-09bc5e79-5a4a-42ab-9475-31dc9a18b45b.png)

