### Human Mobility Patterns

#### Congestion index

**Brief description:** The Congestion index represents the per cent decrease of the hourly average speed observed on the street with respect to the median speed observed during the trimester on that road which is considered the reference speed in normal conditions. Large values (i.e., a congestion index larger than ~30) highlight street congestion (that is, trips feature a lower average speed with respect to the ideal case) while smaller values indicate an ideal travel situation.

**Unit:** percentage

**Value Range:** 0 - 100 [%];

**Color Range:** linear scale [0 - 100]

|Product Name| Human Mobility Patterns Congestion index |
| --- | --- |
| Valid range |Congestion index: 0 - 100 (dimensionless);|
| Temporal resolution | hourly (motorized trip share daily) |
| Temporal coverage | 1 July 2019 - 31 December 2022 |
| Spatial resolution | OSM street edge level (street portion between two consecutive road crossings). |
| Spatial coverage | Austria (9.53, 46.37, 17.16, 49.02) |
| Product description | High-Frequency Location-Based data (HFLB) are one of the most precise proxies of human mobility, as they record the individuals’ device location with an unprecedented level of spatial accuracy and temporal resolution. The collection of HFLB data at national levels unlocks the possibility to characterize the shifts of a population’s mobility patterns throughout long time ranges and with a good level of detail. The "Human Mobility" product builds on HFLB data to provide insights into the population's movement patterns, including the routes taken and the conditions encountered while traveling. The mobility indicators are computed on trajectories created using a generative model that is trained on HFLB data and commuting statistics obtained from census data. The model consists of two components: a Mobility Diary Generator, which creates a sequence of location types that an individual visits in a day, and a Trajectory Generator, which determines the locations based on the individual's home and work location and the general population preferences. The Mobility Diary Generator produces a sequence of stays with defined lengths and location categories (e.g. a user spends 4 hours at home, 6 hours at work, 3 hours at a third location, and 9 hours back at home). Once the mobility diary is generated, the actual locations visited are selected by the Trajectory Generator, which allocates stops to third places (e.g., shopping venues, gyms, restaurants) based on the population density and a realistic travel distance from the previous location, as derived from HFLB data.<br>The generated trips are a series of origin-destination locations with a departing and arrival time attached. To determine the streets where the trip will pass over, a routing query is sent to the Open Source Routing Machine (OSRM) to obtain the sequence of street edges to traverse, the actual traveled distance and travel time without traffic. The values of travel distance and speed returned by OSRM are further compared to the recorded commuting duration of the user to calculate the congestion index. Additionally, the route selection, speed, and other trip characteristics are analyzed to determine the mode of transportation used for each trajectory. The trajectory features are then mapped to a simplified OpenStreetMap road network to identify all the street edges that a specific trajectory traverses. The hourly aggregated values are then computed by aggregating the features of all the trajectories that traverse a street edge during one hour. |
| Source URL | n/a |
| Source DOI | n/a |
| Input datasets |Commercial HFLB data from third parties and public census figures including:<ul><li>resident population by sex and age https://www.statistik.at/en/statistics/population-and-society/population/population-stock/</li><li>number of employed/unemployed, retired, commuters https://www.statistik.at/en/statistics/labour-market/;</li><li>number of students https://www.statistik.at/en/statistics/population-and-society/education/school-attendance/pupils</li></ul>|
| Reported accuracy | The estimation of mobility patterns obtained  from data passively collected by mobile devices presents a challenge in scaling up to accurately depict the movements of a significant portion of the population. Specifically, this is because the data from such devices typically only cover a small percentage of the population and only a limited number of individuals in the dataset exhibit multiple valid trajectories. This limitation stems from a bias in the data collection mechanism, as the adoption rate of mobile devices used to collect the data is not uniform across the population and individuals may only generate digital traces at certain times, depending on their use of GPS location-enabled applications. The accuracy of population count estimates can range from an average confidence interval of ±10% to as high as ±70% in less populated areas, reflecting severe underrepresentation of the resident population. The same limitations apply to the indicators of trajectories, particularly in regards to the count of trajectories and means of transportation detection. The need to expand the empirical dataset to produce a realistic number of population movements enhances the noise and biases present in the original dataset, even with mitigation techniques such as incorporating census data on commuting to adjust the number of trips between locations. |
| License | https://creativecommons.org/licenses/by/4.0/ |

## Disclaimer

Please note that the current indicators on Human Mobility displayed on the platform have not
been yet validated or calibrated to match the real-world scenario. The estimates presented are
intended as placeholders to provide an overview of what the final platform will offer. It is
essential to keep in mind that the estimates are based on data obtained from mobile devices
and, therefore, are susceptible to biases and limitations. For instance, not everyone owns a
mobile device with location-tracking capabilities, which can impact the accuracy and
representativeness of the data. Furthermore, location-based data only cover a small percentage
of the population, which requires the implementation of statistical aggregations and averaging
techniques. As a result, the detection of extreme events (e.g., severe traffic congestion), may be
limited in the output of the analyses.

In summary, while the population presence and human mobility predictions derived from
location-based data can provide valuable insights into human behaviour, they should be used
with caution when drawing conclusions about people's mobility patterns. Specifically, predictions
may not always be accurate, and as such, should be interpreted as an approximation rather
than an exact representation of reality. Anyhow, despite their limitations, population presence
and human mobility predictions can still provide valuable insights into trends and patterns that
can support a comprehensive understanding of human behaviour.

<div align="middle">
  <img alt="Mindearth Logo" src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/gtif-logos/mindearth.png" width="45%" style="vertical-align: middle;"/>
</div>