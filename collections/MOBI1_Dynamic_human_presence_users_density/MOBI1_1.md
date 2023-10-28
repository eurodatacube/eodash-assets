### Dynamic human presence

#### Population density

**Brief description:** The Population Density [#people / km 2 ] reports the hourly density of people
per square kilometer within each Local Administrative Unit (LAU). A larger value denotes a
densely visited area whereas lower values correspond to more sparse (in terms of visitors)
areas. Population density allows us to effectively compare the occupation rate of census areas
featuring different surface extensions and amount of visitors.

**Unit:** people/km2

**Value Range:** GEM level: [0, 10 000]

**Color Range:** logarithmic scale [1, 10 000]


|Product Name| Dynamic human presence |
| --- | --- |
| Valid range | 0 - 100’000 at the Zählsprengel level, 0 - 500’000 at the Gemeinde level. |
| Temporal resolution | hourly |
| Temporal coverage | 1 July 2019 - 31 December 2022 |
| Spatial resolution | Zählsprängel level. |
| Spatial coverage | Austria (9.53, 46.37, 17.16, 49.02) |
| Product description | The steadily growing stream of digital traces logging human activities unlocked the possibility of studying and characterizing human mobility using location-based data passively collected from mobile devices. Amongst other, High-Frequency Location-Based data (HFLB) is one of the most precise proxy of human mobility, as it records the individuals’ devices location with an unprecedented level of spatial accuracy and temporal resolution.<br>The "Dynamic human presence" product leverages HFLB data to estimate thespatial-temporal population dynamics at the Zählsprengel level and hourly time steps.Specifically, it has been derived by concurrently exploiting HFLB (which allows to estimate a prior of the occupation rate of a given unit by counting the number of single devicesobserved within an area at a given time) and census statistics (which report the reference number of residents and in-out commuters per unit) to infer the number of people (or their density) in space and time. This allows overcoming the limitations deriving from the sole employment of static census counts, for example providing a dynamic estimate of the population exposed to natural hazards such as flood or landslides. |
| Source URL | n/a |
| Source DOI | n/a |
| Input datasets |Commercial HFLB data from third parties and public census figures including:<ul><li>resident population by sex and age https://www.statistik.at/en/statistics/population-and-society/population/population-stock/</li><li>number of employed/unemployed, retired, commuters https://www.statistik.at/en/statistics/labour-market/;</li><li>number of students https://www.statistik.at/en/statistics/population-and-society/education/school-attendance/pupils</li></ul>|
| Reported accuracy | The human presence estimates based on data passively collected from mobile devices are known to possibly overestimate population in densely occupied areas while underestimating it in sparsely populated areas. This is due to an inherent bias introduced by the data collection mechanism: the adoption rate of the mobile devices used to collect data is not homogeneous in the population and might depend on the applications installed on the given device (indeed, only some of them provide location data). In general, population count estimates have an average ±10% confidence interval on the projected number that can go up to ±30% relative error in densely populated areas. The confidence interval can extend up to ±70% in less populated areas due to a severe underrepresentation of the resident population. |
| License | https://creativecommons.org/licenses/by/4.0/ |


## Disclaimer

Please note that the provided estimates for Dynamic Human Presence may not be entirely
accurate, mainly due to the collection mechanisms of the data used to generate the estimates.
Indeed, location-based data collected from mobile devices can sometimes overestimate or
underestimate the number of people in a given area, depending on how many mobile devices
are being used and what applications are installed on those devices. This is because not
everyone has a GPS-enabled mobile device, and even those who do have mobile devices might
have different apps installed, which can affect the collected data. Generally, we expect the
population density and count estimates to have a relative error of approximately 10%, which
may increase in very densely or very sparsely populated areas.

<div align="middle">
  <img alt="Mindearth Logo" src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/gtif-logos/mindearth.png" width="45%" style="vertical-align: middle;"/>
</div>
