## Truck detections primary roads

This indicator aims at showing the economic performance of a country by detecting the amount of moving trucks on primary roads in the EU by means of Sentinel-2 cloudless acquisitions between January 2020 and December 2021.  
The detection method (developed by Henrik Fisser - Julius-Maximilians-University Würzburg, Germany) exploits a temporal sensing offset of the [Sentinel-2 multispectral instrument (MSI)](https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-2-msi/msi-instrument),
causing spatially and spectrally distorted signatures of moving objects. 

In order to generally reduce false detections the computation is constrained to road data from [Open Street Maps (OSM)](https://wiki.openstreetmap.org/wiki/Key:highway).
The blue dots in Fig. 1 are examples of identified trucks in these subsets.

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E12c_truck_detections_motorways/E12c_2018-04-19_france.jpg)

*Fig. 1: Truck detection example in southern France*

The Sentinel-2 truck detection method has been validated with [German traffic count stations](https://www.bast.de/BASt_2017/DE/Verkehrstechnik/Fachthemen/v2-verkehrszaehlung/zaehl_node.html)
on the two motorways A3 and A61. This validation implies that the Sentinel-2 method detects in average 78 % of the trucks counted at the four used stations (Fig. 2),
though with some variety. It also suggests that detected objects are mostly trucks and not cars as the number of counted cars at the count stations is approximately three to four times higher than the number of trucks.
Since the station data is hourly, its mean per 15 minutes was calculated for the date and time of the respective Sentinel-2 acquisition.

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E12c_truck_detections_motorways/E12c_validation_percentages.png)

*Fig. 2: Trucks detected by Sentinel-2 vs. station counts [%]*

**Note**
The validation is limited to Germany and an area-specific uncertainty is introduced by potential haze during large-scale processing.
