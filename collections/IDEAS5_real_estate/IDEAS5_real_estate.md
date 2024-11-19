## Real Estate Indicator

This indicator is a combination of satellite and field data.

* For satellite data, the land surface temperature measured from Landsat 8/9 is used. It allows to identify the warmer areas in the city.
* For field data, the French National Database of Buildings is used. It gather information about thousands of building in France. It includes the energy efficiency report, which provides information on the quality of insulation in homes, and economic statistics such as the price per m², which is used as an indicator to classify areas into rich and poor categories.

For data interpretation, the values range from 1 to 6, with 6 representing the highest-risk areas, characterized by poor insulation or LST and a vulnerable population (elderly and economically disadvantaged). The shown values can be filtered using the range slider in the Analysis panel.

Further information can be found [here](https://github.com/sistemagmbh/IDEAS-IDEAS-Libraries/blob/main/indicator5/Sorytelling_RealEstate.md).

Includes the following layers:

- **Land Surface Temperature Indicator**: sub-layers of the indicator, representing the combination of data on population age, social status, and building insulation (or LST depending on the file).
- **Indicator for population age, social status, and building insulation**: sub-layers of the indicator, representing the combination of data on
population age, social status, and building insulation (or LST depending on the file).
- **Heat Risk Indicator**: the intersection of these two sub-layers. It highlights areas where the classifications match in both sub-layers.


- **Spatial coverage : France**
- **Temporal coverage : 1 time**
- **Spatial resolution : 30m**
- **Format : COG product**

V1 - 2024/09/25