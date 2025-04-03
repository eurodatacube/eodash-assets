## Soil Moisture

This indicator shows the distribution of soil moisture acquired by the ESA Earth Explorer [Soil Moisture and Ocean Salinity (SMOS) mission](https://earth.esa.int/eogateway/missions/smos/description). The amount of water held in soil, is crucial for primary production but it is also intrinsically linked to our weather and climate. This is because soil moisture is a key variable controlling the exchange of water and heat energy between the land and the atmosphere. The variability in soil moisture is mainly governed by different rates of evaporation and precipitation. The importance of estimating soil moisture in the root zone is paramount for improving short- and medium-term meteorological modelling, hydrological modelling, the monitoring of plant growth, as well as contributing to the forecasting of hazardous events such as floods.

This dataset is provided by the **Euro Data Cube**'s [SMOS Level-2C Datacube Service](https://collections.eurodatacube.com/smos-datacube/readme.html) offered by Brockmann Consult. The SMOS data cube service is implemented using the [xcube-smos datastore](https://github.com/xcube-dev/xcube-smos), which is available with the permissive MIT license.   

### Dataset description
-  Data is acquired by the sensor onboard SMOS, the [Microwave Imaging Radiometer with Aperture Synthesis (MIRAS)](https://earth.esa.int/eogateway/instruments/miras). MIRAS creates images of radiation emitted in the microwave L-band (1.4 GHz), by measuring soil moisture  observing variations in the natural microwave emission coming up off the surface of the planet.
-  The Level 2 Soil Moisture (SM) product comprises soil moisture measurements geo-located in an equal-area (grid system ISEA 4H9).
-  Spatial resolution: ~40 km (varies due to the SMOS interferometric imaging technique)

### Applications
Soil moisture can be used for various applications, including climate monitoring, weather forecasting, agriculture and water management.

### Read more

* [SMOS L1 and L2 Science data](https://earth.esa.int/eogateway/catalog/smos-science-products)
* [SMOS Datacube Service - Euro Data Cube](https://collections.eurodatacube.com/smos-datacube/)
* [xcube SMOS Python Package](https://xcube-dev.github.io/xcube-smos/)
* [Notebooks for xcube SMOS store](https://github.com/xcube-dev/xcube-smos/tree/main/notebooks)
