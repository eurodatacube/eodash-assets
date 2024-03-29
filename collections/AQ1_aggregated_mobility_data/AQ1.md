Click on a bin on the map to display a scatterplot of your currently selected parameter against Sentinel5-p measurements.

### Disclaimer
This tool allows exploring potential correlations between Sentinel-5P/TROPOMI measurements and human mobility data, with the objective to better understand how people's movement and mobility affects air quality parameters.

For this purpose, both data sources were aggregated to the same spatial grid. For the air quality parameters daily S-5P observations were used. For the mobility data, only observations that preceded the S-5P observation by four hours was considered. Four hours is the typical time that NO2 can remain in the atmosphere and thus be detected.

The mobility data only captures around 22% of the population and is then calibrated with population presence and density. Thus, it is one form of capturing people’s movement but likely not the most suitable. Consequently, estimates provided for Number of Trajectories, Congestion Index, Speed, Motorized Count, and Motorized Share may not be reflecting the reality of mobility on the ground with very high precision.

Being a demonstrator on how to integrate and interactively compare air quality parameters versus mobility statistics, further validation is needed to be able to allow meaningful conclusions.

**Developed with**  
![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/gtif-logos/sistema-mindearth-geosphere.png)
