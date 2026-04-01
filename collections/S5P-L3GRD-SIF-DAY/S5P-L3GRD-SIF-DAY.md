## Solar Induced Fluorescence (SIF) by Sentinel-5P TROPOMI (Daily)
Solar Induced Fluorescence (SIF) is an electromagnetic signal emitted by chlorophyll-a in assimilating plants: part of the energy absorbed by chlorophyll is not used for photosynthesis but re-emitted at longer wavelengths (650–850 nm). Because SIF responds instantaneously to environmental perturbations such as light and water stress, it serves as a direct proxy for photosynthetic activity, offering greater sensitivity than traditional reflectance-based indices such as Normalized Difference Vegetation Index (NDVI). SIF observations (also called TROPOSIF product) from space have emerged as a key resource for evaluating the spatio-temporal distribution of Gross Primary Productivity (GPP) by terrestrial ecosystems, linking carbon and water cycles at global scale.


#### About the dataset
- The SIF product is measured by the [TROPOMI instrument](https://www.tropomi.eu/) aboard ESA’s [Sentinel-5P Precursor](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-5P) satellite.
- SIF is estimated at 740 nm from two fitting windows: 743–758 nm (baseline product, most robust against atmospheric effects) and 735–758 nm (higher precision).
- The product is available as an L2 per-orbit file and as a daily L2B file combining all valid retrievals (qa_value > 0.5) for a given day.
- Only high-quality measurements (qa_value > 0.5) are recommended for further processing.
- More information on the TROPOSIF measurements and quality assessment can be found in the [Product Readme File](https://data-portal.s5p-pal.com/product-docs/troposif/S5P_PUM_PAL_NOV_UPV_SIF_v10.pdf).

#### Use cases
SIF measurements are particularly useful for:
- Monitoring vegetation health, stress, and seasonal cycles globally.
- Estimating gross primary productivity (GPP).
- Studying the response of ecosystems to drought, heatwaves, and land use change.
- Complementing traditional NDVI-based vegetation monitoring with a more direct measure of photosynthetic activity.
