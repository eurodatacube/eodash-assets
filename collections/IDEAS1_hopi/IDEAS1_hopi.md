# Health-Oriented Urban Heat and Pollution Index

Anthropic-induced pollution and climate change consequences as extreme heat waves, makes it essential to develop efficient health indicators.
The Health Oriented Urban Heat and air Pollution Indicator (HOUHPI) indicator is produced by combining four inputs:
* Air pollution
* Urban heat
* Vulnerable population
* Distance to healthcare

On the map white and yellow mean low risk on health , dark red means high risk on health.
In the Analysis panel below you ca use the range slider to filter out values displayed.

Following layers are available to further explore the data:
- **Land surface temperature**: maximum monthly-average land surface temperature per season between 2019
and 2023. We consider that there is a risk for human health above an average 25°C.
- **Number of days per season where air pollution exceeded the WHO threshold** : The indicator takes into account PM2.5,PM10, Ozone and NO2 from CAMS (between 2021 and 2023). If one of the pollutants exceeds the daily threshold, it is considered a polluted day.
- **Distance to nearest hospital or clinic (km)** : computed from the Healthcare Infrastructures indicator with bird's-eye distances.
- **Number of people of age >60 or < 5** : extraction from HDX data and gives information about the number of elderly or children in an area.
- **Health-Oriented Urban Heat and Pollution Index** : sum of the normalized healthcare access and vulnerable population indicators multiplied by the risk factor. The risk factor is computed using
the following knowledge [1] :
    - Air Pollution Risk (APR): Increment of 5% mortality risk when air pollution exceeds WHO thresholds.
    - Urban Heat Risk (UHR): Increment of 6% mortality risk with LST (Land Surface Temperature) above 25°C.
    - Combined Risk (CR): Increment of 21% mortality risk when both conditions are met.
The score goes from 0 for a non existing risk to 2 for a high risk.

Coverage:
- **Spatial coverage:** Europe
- **Temporal coverage:** 3 years (2021 – 2023)
- **Spatial resolution:** 6 km
- **Temporal resolution** : seasonally

V2 - 2024/07/19

[1] https://www.eea.europa.eu/en/newsroom/editorial/combined-effects-of-air-pollution-and-heat-exposure#:~:text=Another%20recent%20study%20identified%20that,exposure%20to%20either%20factor%20on
