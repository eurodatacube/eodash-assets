## Water Turbidity from Sentinel-2

**Turbidity** represents the level of suspended sediments in water also indicating water clarity or how clear is the water. It is mainly caused by the presence of silt, algae in a water body, or industrial waste disposed in the rivers by mining activity, industrial operations, logging, etc. Traditionally, turbidity is analyzed by evaluating water samples however, a good alternative to field survey measurements is satellite remote sensing data, which can capture both spatial and temporal variations in river turbidity levels. Accordingly, the [Copernicus Sentinel-2](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-2) multispectral can be employed to monitor and evaluate changes in rivers.

### Case study: Monitoring Po River turbidity
This study examined the Po River basin, from Ferrara to the river mouth, where freshwater and saltwater mix. Sentinel-2A and 2B images (2019–2022) covering 3700 km² were analyzed. Using [ACOLITE](https://github.com/acolite/acolite) algorithm, 42 cloud-free images were processed to create 10 m resolution turbidity maps. These maps correlated with Po River discharge data from [Environmental Protection Agency of the Region of Emilia Romagna (ARPA-ER)](https://www.arpae.it/it) and water levels from [AIPO](https://www.agenziapo.it/). 

### Interperting images:
- Units metric: Formazin Nephelometric Unit (FNU) - are a metric to measure turbidity by the scattered light method
- Colore range interpretation: ranging from low FNU (blue/green) to higher FNU (yelllow-red)

Find more about this case study, and main conclusions about Water Connectivity and Turbidity Patterns, as well as exposed riverbeds on a [dedicated story](https://race.esa.int/story?id=po-river-discharge).



