# HydroPower

The hydro power (reservoir) module is used to present reservoir surface area, level and storage changes. First, we analyze individual reservoirs extracting water area from pre-processed optical and SAR satellite imageries using a machine learning algorithm. After outlier filtering and post-process, the timeseries graph are constructed for each individual reservoir. Where there is a cross-section with Sentinel 3A/B orbits the reservoir water levels are directly obtained from satellite altimetry. Where only SWE time series exist the storage level is estimated based on the nominal change in surface water area.

## SWE

|Product Name| Surface Water Extent (SWE)|
| --- | --- |
| Spatial resolution | 10m |
| Temporal reference | Monthly, 2017-2022 |
| Value range | - |
| Spatial coverage | Selected reservoirs in Austria |
| Product description | The SWE product is derived from continuous observations of high-resolution radar and optical data. It is based on a multivariate logistic regression model to estimate the surface water probability from Sentinel-1 and Sentinel-2 imagery. The dual sensor approach acknowledges the limitations to surface water mapping when relying solely on either optical or SAR based instruments and aims to take advantage of the individual sensors strengths while minimizing their weaknesses. The surface water product has higher spatial resolution (10 m) compared to the existing products, is not impacted by cloud coverage, and can be run in near-real time to detect surface water changes at national scale. |
| Source URL | https://www.mdpi.com/2072-4292/13/9/1663 |
| Source DOI | https://doi.org/10.3390/rs13091663 |
|Input datasets| Sentinel-1 and Sentinel-2|
| Reported accuracy |>90% overall accuracy|
| License | Creative Commons CC BY-SA 3.0 IGO|

![DHI Logo](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/gtif-logos/dhi.png "DHI Logo")
