## Cloud Fraction (CF) by Sentinel-5P TROPOMI (Monthly)
The Cloud Fraction (CF) quantifies the **portion of a satellite pixel covered by clouds**, providing a measure of cloud coverage at a given location. Cloud fraction is a key parameter for understanding the impact of clouds on radiation, weather, and atmospheric composition.
CF is especially important for satellite trace gas retrievals, as clouds can obscure or scatter the atmospheric signal. Accurate knowledge of cloud coverage ensures the reliability of measurements for gases like ozone, nitrogen dioxide, and methane.
CF provides a **horizontal coverage metric** rather than vertical structure, complementing other cloud parameters such as[Cloud Top Height (CTH)](https://eodashboard.org/explore/?x=0.0000&y=0.0000&z=2.5934&template=expert&indicator=S5P-L3GRD-CLOUDTH-DAY&datetime=2025-02-28).

#### About the dataset

- The CF product is derived from measurements by the [TROPOMI instrument](https://www.tropomi.eu/) aboard Copernicus ESA's [Sentinel-5P Precursor](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-5P) satellite.
- The measurements are aggregated into monthly composites. 
- More information on the Tropomi cloud product measurements and quality assessment can be found in the [Product Readme file](https://sentiwiki.copernicus.eu/__attachments/1673595/S5P-MPC-DLR-PRF-CLOUD%20-%20Sentinel-5P%20Cloud%20Level%202%20Product%20Readme%20File%202025%20-%202.10.pdf).

#### Use cases
The CF product, combined with [Cloud Top Height (CTH)](https://eodashboard.org/explore/?x=0.0000&y=0.0000&z=2.5934&template=expert&indicator=S5P-L3GRD-CLOUDTH-DAY&datetime=2025-02-28),, provides a comprehensive view of cloud properties, supporting both operational and scientific applications in atmospheric monitoring. Monthly composites are particularly useful for tracking seasonal cloud cycles, long-term trends in cloud coverage, and regional climate patterns. Some applications of this CF product are:

- Improving trace gas retrievals by correcting for cloud contamination
- Monitoring cloud coverage at regional and global scales over time
- Climate studies: cloud-radiation interactions, cloud feedbacks, and long-term trends
- Weather analysis: seasonal cloud distribution and convection patterns
- Validation of atmospheric models and satellite cloud retrieval algorithms
