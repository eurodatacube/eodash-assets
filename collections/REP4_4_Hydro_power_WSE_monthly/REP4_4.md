# HydroPower

The hydro power (reservoir) module is used to present reservoir surface area, level and storage changes. First, we analyze individual reservoirs extracting water area from pre-processed optical and SAR satellite imageries using a machine learning algorithm. After outlier filtering and post-process, the timeseries graph are constructed for each individual reservoir. Where there is a cross-section with Sentinel 3A/B orbits the reservoir water levels are directly obtained from satellite altimetry. Where only SWE time series exist the storage level is estimated based on the nominal change in surface water area.

# WSE

|Product Name| Water Surface Elevation (WSE)|
| --- | --- |
| Spatial resolution | Individual reservoirs |
| Temporal reference | May 2019 to Dec. 2022 |
| Value range | - |
| Spatial coverage | Virtual stations |
| Product description | Water levels are estimated using satellite-based altimetry measurements. Altimetry is essentially a ranging technique measuring the time it takes for a pulse to bounce of the ground and return to the satellite sensor. Measurements can only be taken at nadir and the size of the footprint can be rather large affecting the minimum size of the reservoirs that can be monitored. As a consequence, the technology only provides information for selected reservoirs and apart from size then the orientation and the nature of near-by terrain will dictate whether the water levels of a reservoir can be monitored. |
| Source URL | https://browser.creodias.eu/ |
| Source DOI | N/A |
|Input datasets| Sentinel-3A/B|
| Reported accuracy |The accuracy of altimetry measurements varies depending on the type and size of the reservoir, as well as on the location and the topography at the area of interest. For large reservoirs with no terrain interference accuracies of less than 5 cm is obtainable. Smaller reservoirs or larger reservoirs with terrain interference will all have larger errors (several tens of centimeters).|
| License | Creative Commons CC BY-SA 3.0 IGO|

![DHI Logo](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/gtif-logos/dhi.png "DHI Logo")
