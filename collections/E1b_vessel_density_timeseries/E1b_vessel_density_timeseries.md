## Vessel density time series

This indicator aims at showing ships detected in the major EU ports by means of Copernicus Sentinel-1 data.
A vessel density map is produced by deriving, for each 1 km2 pixel of the masked image of the selected area, an index given by the ratio:

density_vessels= 1000 * number_vessels / number_observations

where the number of observations corresponds to the intersection of all the satellite footprints of the selected month.

The figures below show a comparison with the corresponding map provided by [EMODnet](https://race.esa.int/?x=1040481.31544&y=5968190.74701&z=4.29471&poi=World-E13o&search=World%3A+Vessel+density+%28all%29+%5Bh%2Fsqkm%5D) using the Structural Similarity Index (SSIM).


![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E1b_vessel_density_timeseries/E1b-img1.png)
*Sentinel-1 based indicator*

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E1b_vessel_density_timeseries/E1b-img2.png)
*EMODnet indicator*


The detection algorithm has been developed by: 
###
- Alessandro Cimbelli
