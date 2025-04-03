## Ocean Salinity

This indicator shows the sea surface salinity globally acquired by the ESA Earth Explorer [Soil Moisture and Ocean Salinity (SMOS) mission](https://earth.esa.int/eogateway/missions/smos/description). Ocean currents are driven by temperature and salinity variations in the seawater and Understanding ocean salinity's annual and inter-annual variability are crucial in understanding the role of the ocean in the climate system. Ocean circulation is mainly driven by the water and heat flux through the atmosphere-ocean interface, but salinity is also fundamental in determining ocean density and hence thermohaline circulation. 

This dataset is provided by the **Euro Data Cube**'s [SMOS Level-2C Datacube Service](https://collections.eurodatacube.com/smos-datacube/readme.html) offered by Brockmann Consult. The SMOS data cube service is implemented using the [xcube-smos datastore](https://github.com/xcube-dev/xcube-smos), which is available with the permissive MIT license.   

### Dataset description
-  Data is acquired by the sensor onboard SMOS, the [Microwave Imaging Radiometer with Aperture Synthesis (MIRAS)](https://earth.esa.int/eogateway/instruments/miras). MIRAS creates images of radiation emitted in the microwave L-band (1.4 GHz), by measuring changes in the salinity of seawater by observing variations in the natural microwave emission coming up off the surface of the ocean.
-  The Level 2 Ocean Salinity (OS) product comprises sea surface salinity measurements geo-located in an equal-area (grid system ISEA 4H9).
-  Spatial resolution: ~40 km (varies due to the SMOS interferometric imaging technique)

### Applications
Ocean salinity can be used for various applications, including ocean circulation, climate monitoring and water management.

### Read more

* [SMOS L1 and L2 Science data](https://earth.esa.int/eogateway/catalog/smos-science-products)
* [SMOS Datacube Service - Euro Data Cube](https://collections.eurodatacube.com/smos-datacube/)
* [xcube SMOS Python Package](https://xcube-dev.github.io/xcube-smos/)
* [Notebooks for xcube SMOS store](https://github.com/xcube-dev/xcube-smos/tree/main/notebooks)
