# Finished goods production: vehicles inventory level

This indicator aims at tracking production and movement at factories and ports importing and exporting cars to monitor the increase and decrease of new car production
by combining satellite data from:
###
- PALSAR-2, which uses L-band SAR mounted on [JAXA](https://global.jaxa.jp/)'s ALOS-2 
- C-band SAR mounted on the [ESA](https://esa.int/)'s Sentinel-1
- NASA-processed high-resolution optical remote sensing data from Planet’s SkySat



### Change in the number of new car at automobile factory

All over the world, countries have taken measures to reduce the spread of the coronavirus, such as urban lockdowns or stay-at-home requests due.
Automotive manufacturers around the world also have taken steps, such as adjusting, reducing and suspending new car production.


The area bordered by a red rectangle in Fig. 1 shows temporal changes in the density of new cars parked at an automobile factory near Beijing Airport, China from December 2019 to May 2020. During the lockdown in Beijing, from January to March 2020, the density of new cars dropped significantly. 

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E9_car_containers/Tri_E8.png)

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E9_car_containers/Tri_1_E8.png)



## Change in the number of car containers at shipping terminals Japan


Situated at the innermost edge of Ise Bay, which is located at the center of the Japanese Archipelago facing the Pacific Ocean, the Port of Nagoya has steadily grown since it opened for international trade on Nov. 10, 1907. The Port of Nagoya handles all types of cargo (general, container, bulk, etc.) and is the largest port in Japan in terms of total cargo throughput, reaching 197 million tons in 2018, according to the Port of Nagoya Authority. In addition, the Port of Nagoya leads in Japanese automobile exports: approximately 1.4 million completed automobiles move through there annually. 

From November 2019 to June 2020, the Japanese Aerospace Exploration Agency’s (JAXA) ALOS-2 satellite observed the density of car containers at Shimpomachi Terminal in the port of Nagoya to monitor the condition of industrial trade. During the novel coronavirus pandemic, ALOS-2 observations show that shipments of new cars decreased. 

Figure 1 shows the difference in the containers at the Shipomachi Terminal between November 2019 (blue) and May 2020 (red).


![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E9_car_containers/JP02-E9-Fig1.png)

*Figure 1. ALOS-2 3-meter composite color image at Shimpomachi, Port of Nagoya (red color: May 8, 2020 and blue color: Nov. 27, 2019).*

Figure 2 shows car container density change in a time series GIF from November 2019 to June 2020, with animation data by ALOS-2. 

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E9_car_containers/JP02-E9-Fig2.gif)

*Figure 2. ALOS-2 time series data*

Figure 3 shows the density of car containers in the ALOS-2 and Sentinel-1 image since the end of November 2019 to October 2020. The density dropped around March and has been lower until the end of August. According on the report of the Nagoya Port Customs, it was also confirmed that the amount of exports had been declining since March. We found the car density level might be slow down and bottomed in August as well as the trend might be turned around October by satellite image analysis. 

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E9_car_containers/JP02-E9-Fig3.png)

*Figure 3. The car container density change in Shimpomachi in the Port of Nagoya, Aichi, Japan using data fused from the JAXA ALOS-2 satellite and the European Space Agency’s (ESA) Sentinel-1 satellite*

### Change in the number of new car / containers at container terminal Singapore

Earth-observing satellites have tracked activity at global ports importing and exporting cars and other shipping containers. While data indicate an overall decline in such activity at Singapore’s Tanjong Pagar and Keepel Terminals during coronavirus-related shutdowns, a large, temporary facility can be seen at the Tanjonh Pagar Terminal. This likely is to house as many as 15,000 COVID-19 patients and foreign workers. 

Figure 1 shows ALOS-2 ScanSAR mode data superimposed with Sentinel-1 data at Singapore port on April 22, 2020

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E9_car_containers/E9_Fig1.png)

*Figure 1 Port of Singapore*

Temporal changes in the density of new cars and containers at the container terminal such as Tanjong Pagar Terminal in Singapore port are monitored from January to May 2020, shown in Figure 2 using Sentinel-1 and ALOS-2 data.

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E9_car_containers/E9_Fig2.png)

*Figure 2 Time series SAR data in container terminal in Singapore from January to May 2020*

Figures 3 and 4 show car and container density-change graphs derived from time series SAR data in Tanjong Pagar Terminal and Keepel terminal area at the port of Singapore. Figure 3 shows the density of car/containers dropping from the end of April in Tanjong Pagar Terminal. A large temporary facility can be seen in the image of Tanjong Pagar Terminal. The Singapore government announced that it will potentially house as many as 15,000 COVID-19 patients and foreign workers, as the number of coronavirus cases in Singapore continues to increase. 

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E9_car_containers/E9_Fig3.png)

*Figure 3 Tanjong Pagaor terminal*

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E9_car_containers/E9_Fig4.png)

*Figure 4 Keppel terminal*


## International space agencies see fewer cars in pay parking area at Los Angeles International Airport during pandemic-related slowdown

Satellite imagery from three international space agencies has quantified the decline in traffic at Los Angeles International Airport (LAX) since COVID-19 slowdowns began, specifically noting both the lower number of cars in the pay parking lot and the consistency of these numbers throughout the day.

As recently as April 2020, imagery from NASA, JAXA and ESA showed significant fluctuations in the number of cars in the lot at different times of day. This pattern aligns with what would be expected with travelers flying at various times throughout the week and during the winter holidays. Since pandemic safety restrictions brought travel to a near-standstill, however, the consistency of parked cars indicates that fewer cars are moving in and out of the lots nearby the airport.

The report from LAX is part of an effort by NASA, JAXA and ESA to help quantify changes at airports and other transportation hubs around the world caused by lockdowns designed to prevent the spread of the novel coronavirus. Scientists are combining two kinds of space-based remote sensing data – synthetic aperture radar (SAR) data from JAXA’s ALOS-2 and ESA’s Copernicus Sentinel-1 satellites, with NASA-processed high-resolution optical remote sensing data from Planet’s SkySat. Planet provides data to NASA as part of the agency’s Commercial SmallSat Data Acquisition Program. 

Combining these datasets enables production of more comprehensive assessment of changes in patterns in the airport parking lots. While Planet imagery can be used to monitor changes in the number of cars in these lots and around the world every day, its camera like sensors cannot see through clouds, therefore limiting our ability to track changes on cloudy or rainy days. The radar systems on the Sentinel-1 and ALOS-2SAR satellites penetrate through clouds and rain, as well as making observations both during the day and at night. This capability makes it possible to track changes in activity, such as parking patterns, every time a SAR satellite is over the region – a few times a week.  The combined datasets make it possible to better track changes in human activity related to the COVID-19 than with a single satellite system.    

The time series trend graph of car density in the parking area at LAX shown in Figure 1 tracks the total number of cars during December 2019 and September 2020. 

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E9_car_containers/US021-E9-Fig1.png)

*Figure 1. Car density graph during December 2019 and September 2020.*

In April, as the effects of California’s earlier pandemic-related lockdowns were just taking hold, ALOS-2 and Sentinel-1 recorded variations in the number of cars parked at LAX. This was largely due to the 6-hour time differences between observations between ALOS-2 and Sentinel-1. Sentinel-1 passes over LAX at 6 a.m. and 6 p.m. (PST), and ALOS-2 at noon and midnight (PST). Since then, however, the variation in the number of cars between observations for both satellites has stabilized, indicating both fewer cars overall and fewer cars leaving and entering the parking area.

Figure 2 shows a color composited SAR image of LAX from the PALSAR-2 instrument aboard the ALOS-2 satellite. The different colors in the image correspond to the different dates the images were captured. The blue/green area shows cars parked in the pay lots on Jan. 11, before the pandemic restrictions. Red areas indicate fewer cars parked there on May 30. White areas are buildings.

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E9_car_containers/US021-E9-Fig2.png)

*Figure 2. ALOS-2 LAX data.*

Figures 3 shows car detection in red using Planet’s SkySat imagery and Artificial Intelligence (AI). The number of cars in the rental car lots remained high, indicating less demand for those vehicles.


![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E9_car_containers/US021-E9-Fig4.png)

*Figure 3 Car number estimation in July Planet SkySat and AI*

Overall, Planet’s SkySat estimated 3,708 cars parked on January 9 2020 and 1,943 on July 8 2020. This corresponds with SAR data from ALOS-2 and Sentinel-1. 

As a result of the temporal analysis for  car  detection near LAX, the car density has increased since March 2021. 
According to the [statistics for LAX](https://www.lawa.org/lawa-investor-relations/statistics-for-lax), the numbers  of  passengers and rental cars for LAX had still declined  in  the early months of 2021, but turned to increase in May 2021 compared  to  May 2020. 
