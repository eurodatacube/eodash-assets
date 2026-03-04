## Anthropogenic SO₂ COBRA (PBL) by Sentinel-5P TROPOMI (Daily)

The Anthropogenic SO₂ COBRA product provides measurements of **sulfur dioxide in the planetary boundary layer (PBL)**, capturing emissions primarily from human activities such as fossil fuel combustion and industrial processes. 

#### About the dataset
- The Anthropogenic SO₂ COBRA product is measured by the [TROPOMI instrument](https://www.tropomi.eu/) aboard Copernicus ESA's [Sentinel-5P Precursor](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-5P) satellite, operating in the UV spectral range.
- This product uses the Covariance-Based Retrieval Algorithm (COBRA), implemented operationally in November 2024, which improves retrieval quality by reducing noise and bias compared to traditional Differential Optical Absorption Spectroscopy (DOAS) methods. Large SO₂ concentrations are still retrieved using DOAS in alternative spectral fit windows.
- Provides the SO₂ vertical column in the PBL, with optional total vertical columns at 1 km, 7 km, and 15 km altitudes.
- Includes random and systematic errors, as well as a quality assurance flag (qa_value). Pixels with qa_value > 0.5 are recommended for reliable analysis.
- Data are daily gridded measurements, suitable for monitoring emissions and air quality at global scales.
- Reprocessed data (RPRO, version 2.7.0) are available from the start of the mission up to November 2024.

#### Use cases
The COBRA PBL SO₂ product is useful for:
- Monitoring anthropogenic SO₂ emissions and industrial hotspots.
- Air quality assessment and pollution modeling.
- Tracking transport and dispersion of sulfur dioxide plumes.
- Climate research, including aerosol–cloud–radiation interactions.
