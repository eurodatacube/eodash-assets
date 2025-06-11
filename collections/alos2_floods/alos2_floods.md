# Flood mapping in East Africa
This flooding map was created using ALOS-2 data. ALOS-2 is a JAXA satellite equipped with a radar sensor called PALSAR-2, which can capture images of the surface day or night, even through clouds. This makes it very useful to monitoring floods, since it can detect water regaadless of weather conditions. In radar images, flooded areas appear da in because smooth water reflects the radar signal away from the satellite. 
The dataset shows flooded areas marked in red, after the passing of Cyclone Teddy in 2023.

## Dataset Description
- Coverage: Maps of flood were computed for both open area (i.e. bare soil) and urban area. Two different methods were applied to detect this two complementary types of flood.
- Metric: Flood extent and intensity derived from spatial grids and imagery analysis, with temporal layering for tracking flood evolution.
- Processing steps: radar HH polarization was pre-processed (noise removed, speckle filterin) and after that a threshould was applied - values below XXX were considered to be water. Finally a mask was applied to remove peramente water bodies.
