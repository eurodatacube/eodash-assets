## Truck detections primary roads

This indicator shows moving trucks on EU primary roads detected in Sentinel-2 cloudless imagery between January 2020 and December 2021.  
The detection method enables to detect trucks on a large scale using Sentinel-2 data and was developed in the context of the of the [ESA COVID-19 Custom Script Contest](https://www.esa.int/Applications/Observing_the_Earth/COVID-19_how_can_satellites_help) by Henrik Fisser - Julius-Maximilians-University Würzburg, Germany.

The method exploits an effect related to the [Sentinel-2 Multispectral Instrument (MSI)](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-2/Instrument) geometry. Sentinel-2 does not see a moving truck once but three times in the red-blue-green wavelengths. As the truck keeps traveling during this short time offset, it appears spectrally disassembled. This pattern may be used for detecting roaming trucks on roads. Although visual inspection cannot confirm that the objects are trucks, this is implied by the ratio between size of different vehicles and a Sentinel-2 pixel (see validation for details). However, a confusion with moving vehicles of similar size such as buses may occur.

In order to generally reduce false detections the computation is constrained to road data from [Open Street Maps (OSM)](https://wiki.openstreetmap.org/wiki/Key:highway).
The blue dots in Fig. 1 are examples of identified trucks in these subsets.

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E12c_truck_detections_motorways/E12c_2018-04-19_france.jpg)

*Fig. 1: Truck detection example in southern France*

The Sentinel-2 truck detection method has been validated with [German traffic count stations](https://www.bast.de/DE/Themen/Digitales/HF_1/Massnahmen/verkehrszaehlung/verkehrszaehlung.html?nn=427910)
on the two motorways A3 and A61. This validation implies that the Sentinel-2 method detects in average 78 % of the trucks counted at the four used stations (Fig. 2),
though with some variety. It also suggests that detected objects are mostly trucks and not cars as the number of counted cars at the count stations is approximately three to four times higher than the number of trucks.
Since the station data is hourly, its mean per 15 minutes was calculated for the date and time of the respective Sentinel-2 acquisition.

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E12c_truck_detections_motorways/E12c_validation_percentages.png)

*Fig. 2: Trucks detected by Sentinel-2 vs. station counts [%]*

**Note**
The validation is limited to Germany and an area-specific uncertainty is introduced by potential haze during large-scale processing.
