|Product Name| Distance to Settlement (Satellite-based) |
| --- | --- |
| Spatial resolution | 10m |
| Temporal reference | 2019 |
| Value range | 2 - 5,040 (m) |
| Spatial coverage | Austria (9.5°, 46.3°, 17.2°, 49.0°) |
| Product description | This product uses the World Settlement Footprint (WSF) 2019 to identify the location of settlements. The World Settlement Footprint (WSF) 2019 is a 10m resolution binary mask outlining the extent of human settlements globally derived by means of 2019 multitemporal Sentinel-1 (S1) and Sentinel-2 (S2) imagery. Distances to the closest settlements are calculated in meters for every grid cell at 10x10m resolution.<br>Based on the hypothesis that settlements generally show a more stable behavior with respect to most land-cover classes, temporal statistics are calculated for both S1- and S2-based indices. In particular, a comprehensive analysis has been performed by exploiting a number of reference building outlines to identify the most suitable set of temporal features (ultimately including 6 from S1 and 25 from S2). Training points for the settlement and non-settlement class are then generated by thresholding specific features, which varies depending on the 30 climate types of the well-established Köppen Geiger scheme. Next, binary classification based on Random Forest is applied and, finally, a dedicated post-processing is performed where ancillary datasets are employed to further reduce omission and commission errors. Here, the whole classification process has been entirely carried out within the Google Earth Engine platform.|
| Source URL | https://download.geoservice.dlr.de/WSF2019/  |
| Source DOI | https://doi.org/10.1553/giscience2021_01_s33 |
|Input datasets| Sentinel-1 and Sentinel-2|
| Reported accuracy | The WSF2019 has been validated against 1M ground-truth samples collected – with the support of Google and Mapswipe - by crowdsourcing photointerpretation of reference very high-resolution satellite imagery. Accuracy report is pending publication. |
| License | https://creativecommons.org/licenses/by/4.0/ |
| WMS | https://geoservice.dlr.de/eoc/land/wms?SERVICE=WMS%26REQUEST%3DGetCapabilities  |