# Lake extension monitoring

Monitoring lake extension is crucial for understanding ecosystem health, water resource management, and climate change impacts. Lakes are vital habitats that support biodiversity and provide resources for communities. Tracking changes in lake size and extent helps identify trends related to seasonal variations, drought, or flooding, enabling effective management of water resources. 

The JAXA's satellite ALOS-2, allows to monitor thanks to the PALSAR-2 sensor onboard. PALSAR-2 is a Synthetic Aperture Radar (SAR), allows to monitor which emits microwave and receives the reflection from the ground to acquire information. Since it does not need other sources of light such as the sun, SAR has the advantage of providing satellite images regardless day or night. The frequency of transmitting and receiving microwave is L-band, which is less affected by clouds and rains. This all-weather observing capability is suitable for monitoring disasters rapidly. In addition, L-band microwave can reach to the ground partially penetrating through vegetation to obtain information of vegetation and ground surface.

## Interpreting radar images
In radar images from ALOS-2, different colors or grayscale tones represent the backscatter intensity, which indicates the type of surface or feature:
- Dark Shades (Black/Dark Gray): These regions indicate water bodies, such as lakes, rivers, and wetlands. Water absorbs radar signals, resulting in minimal backscatter, creating a dark appearance.
- Lighter Shades (Gray/White): These shades represent land surfaces or areas with high backscatter, such as vegetation, soil, or urban structures. The lighter the shade, the more reflective or rough the surface is to the radar signal.

## Dataset description
- Coverage: Global, focusing on regions with lakes, wetlands, and other water bodies. PALSAR-2’s orbit provides frequent, detailed coverage of these areas.
- Metric: The dataset uses SAR backscatter intensity to measure surface features, including water extent and land cover. SAR's resolution allows for detailed imaging of both small and large lakes.
- Temporal Coverage: Continuous data collection since 2014, with regular revisit times. This multi-year dataset supports long-term monitoring of water bodies and hydrological changes.
- Spatial Resolution:
  - Spotlight Mode: 1 m x 3 m resolution for a 25 km x 25 km swath, allowing for highly detailed imaging of smaller lakes.
  - Stripmap Mode: Minimum resolution of 3 m for a 50 km swath, with options for 10 m and 6 m resolution for larger swaths of 70 km, enabling effective monitoring of medium to large water bodies.
  - ScanSAR Mode: Provides resolutions of 60 m and 100 m for swaths of 490 km and 350 km, respectively, suitable for broader regional assessments.
