## Automobile inventory time series

This indicator aims at showing inventory level at various motor vehicle production sites by means of Synthetic Aperture Radar satellites such as the C-band [Copernicus Sentinel-1](http://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-1).
The indicator shows a rolling mean of the SAR backscatter signal over the logistic areas. 

The Sentinel-1 GRD IW time series are extracted for each AOI (area of interest), using same orbit for the whole time series. The HV cross-polarization is used as it is more sensitive to rough surfaces. 
An average value is computed for the AOI at each observation date.

