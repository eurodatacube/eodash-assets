##  Volcanic SO₂ (7km) NRT by Sentinel-5P TROPOMI (Daily)
The Volcanic SO₂ (7km) Near Real-Time (NRT) product measures sulfur dioxide concentrations primarily from volcanic sources, retrieved assuming SO₂ is located at an altitude of 7 km in the atmosphere. This product provides daily snapshots of volcanic degassing and eruption plumes within the last seven days, enabling near-real-time monitoring of volcanic activity and the rapid tracking of sulfur-rich emissions.

#### About the dataset

- The Volcanic SO₂ (7km) NRT product is measured by the  [TROPOMI instrument](https://www.tropomi.eu/) aboard Copernicus ESA's [Sentinel-5P Precursor](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-5P) satellite, operating in the UV spectral range.
- The retrieval assumes SO₂ is located in a layer at 7 km altitude, making it particularly suited for detecting elevated volcanic plumes injected into the free troposphere.
- Only the last seven days of data are provided as NRT maps, making this product ideal for operational monitoring of ongoing volcanic events.
- Only pixels where a volcanic source is most likely (sulfurdioxide_detection_flag > 0) and where the solar zenith angle is within limits (SZA < 70°) are included. Note that SO₂ from potential anthropogenic sources has not been filtered out and can therefore still appear in the data.
- More information on the TROPOMI SO₂ measurements and quality assessment can be found in the [Product Readme file](https://sentiwiki.copernicus.eu/__attachments/1673595/S5P-MPC-BIRA-PRF-SO2-Sentinel-5P-Sulphur-Dioxide-Readme-2025-2.11.pdf). The dataset is available via [STAC Browser](https://radiantearth.github.io/stac-browser/#/external/data-portal.s5p-pal.com/api/s5p-l3/so2-cobra-pbl).


####  Use cases
The Volcanic SO₂ (7km) NRT product is useful for:
- Rapid response monitoring of volcanic eruptions and passive degassing activity globally.
- Tracking the short-term transport of volcanic SO₂ plumes in near real-time.
- Aviation safety: early detection of sulfur-rich ash and gas clouds that pose risks to aircraft.
