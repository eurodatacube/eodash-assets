## Water Turbidity from Sentinel-2

Satellite-based turbidity products from [Sentinel-2 MSI](https://s2.pages.eopf.copernicus.eu/pdfs-adfs/MSI/L2/PDFS_S2_MSI_L2.myst.html) reveal water variability in the upper Adriatic region. This study examined the Po River basin, from Ferrara to the river mouth, where freshwater and saltwater mix.
Sentinel-2A and 2B images (2019–2022) covering 3700 km² were analyzed. Using [ACOLITE](https://github.com/acolite/acolite) algorithm, 42 cloud-free images were processed to create 10 m resolution turbidity maps. These maps correlated with Po River discharge data from ARPA-ER and water levels from AIPO. 


#### Water Connectivity and Turbidity Patterns

Between 2019–2022, discharge at Pontelagoscuro ranged from 104 to 8011 m³/s. Six discharge ranges were defined: dry (<500 m³/s) to extreme flood (>6000 m³/s). Turbidity values (0–400 FNU) varied with discharge. For instance, on October 26, 2019, a discharge of 3862 m³/s caused turbidity over 200 FNU downstream. Low discharge (e.g., April 28, 2022) showed high turbidity (~350 FNU) due to tidal effects.

Turbidity fronts shifted upstream during dry conditions from tidal currents and seawater intrusion.

### Detecting Drought Impacts via Satellites

The 2022 drought revealed exposed riverbeds, emphasizing satellites' role in detecting low water levels and aiding navigation.


## Machine Learning for Coastal Analysis

Deep feed-forward neural networks (DFNNs) analyzed chlorophyll-a (CHL) anomalies in the Northern Adriatic Sea. SHapley Additive exPlanation (SHAP) highlighted CHL as the most important feature. Offshore, wind velocity influenced mixing, while nearshore, Po River discharge dominated. Wavelength-specific reflectance revealed simpler offshore versus complex nearshore water types.

