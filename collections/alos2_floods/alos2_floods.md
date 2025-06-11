# Flood mapping in East Africa
This flooding map was created using ALOS-2 data to show the extent of floodings in the 'Horn of Africa' region, after above-average rainfall caused by [El Niño in 2023](https://eodashboard.org/). 

[ALOS-2 is a JAXA](https://www.eorc.jaxa.jp/ALOS-2/en/about/palsar2.htm) satellite equipped with a Synthetic Aperture Radar (SAR) sensor called PALSAR-2,which emits microwave and receives the reflection from the ground to acquire information. Since it does not need other sources of light such as the sun, SAR has the advantage of providing satellite images regardless day or night. This makes it very useful to monitoring floods, since it can detect water regaadless of weather conditions. In SAR images, flooded areas appear darker that the surrounding land because smooth water reflects the radar signal away from the satellite. 

## Dataset interpretation
- Flooded areas are **marked in red**.

## Dataset Description
- Coverage: Mozambique Area
- Processing steps: radar HH polarization was pre-processed (noise removed, speckle filterin) and after that a threshould was applied - values below XXX were considered to be water. Finally a mask was applied to remove peramente water bodies.
