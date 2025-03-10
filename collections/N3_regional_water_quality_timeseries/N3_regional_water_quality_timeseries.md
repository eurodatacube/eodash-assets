## Water Quality Time Series

Chlorophyll-a (Chl-a) concentration is an indicator of algae abundance which fluctuates naturally over space and time, as a result of combined atmospheric and oceanic effects (e.g., marine currents and upwelling). In coastal areas, strongly influenced by river inputs and human activities, high Chl concentration can result from the discharge of urban sewage, industrial runoffs, and fertilizers from agriculture activities over watersheds. In particular, nutrient inputs of anthropogenic origin affect the natural amount of phytoplankton in marine and inland waters, representing a continuous threat to biodiversity and leading to undesirable modifications of phytoplankton concentration (i.e., eutrophication).

The time series shows weekly Chl-a concentration offshore the Venice lagoon (45.30 N, 12.50 E) as calculated from [Sentinel-3](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-3-olci) full resolution (250m) data:

* Green dots show weekly values lower than the climatological mean (in black), indicating good water quality.
* Blue dots show weekly values greater than the climatological mean but still inside the climatological variability, indicating regular water quality.
* Red dots stand for values beyond the climatological variability, indicating poorer water quality.

## Ocean Colour Algorithm

Weekly Chlorophyll (CHL) and Total Suspended Matter (TSM) concentrations rely on Sentinel3-OLCI (A and B) full spatial resolution observations (300 m). We collected the CHL full time series (May 2016 – to present) of Sentinel3-OLCI data from the Copernicus Marine Service:
- Mediterranean Sea
  - OCEANCOLOUR_MED_BGC_L3_NRT_009_141 (https://doi.org/10.48670/moi-00297)
  - OCEANCOLOUR_MED_BGC_L3_MY_009_143 (https://doi.org/10.48670/moi-00299)
- Black Sea
  - OCEANCOLOUR_BLK_BGC_L3_NRT_009_151 (https://doi.org/10.48670/moi-00301)
  - OCEANCOLOUR_BLK_BGC_L3_MY_009_153 (https://doi.org/10.48670/moi-00303)

The Copernicus Marine CHL products (for both Mediterranean and Black Sea) are operationally produced in near-real time by the CNR-ISMAR-GOS (Italian National Research Council – Institute of Marine Sciences – Group of Satellite Oceanography).
TSM data are specifically produced by CNR-ISMAR-GOS for the ESA-RACE Dashboard starting from Sentinel3-OLCI L2 data distributed by [EUMETSAT].(https://data.eumetsat.int)

Phytoplankton chlorophyll retrieval is based on regionals algorithms: Volpe et al. (2019), adapted to OLCI bands (the algorithm exploits the 555 nm band, while OLCI has the band centred over the 560 nm channel), for Mediterranean Sea, and an ensemble algorithm based on band-ratio algorithm (B/R) (Zibordi et al., 2015) and a Multilayer Perceptron (MLP) neural net based on Rrs values at three individual wavelengths (490, 510 and 555 nm) (Kajiyama et al., 2018; Colella et al., 2021). TSM derives from normalised water-leaving reflectance at OLCI bands (400, 674 and 709 nm) via the Inverse Radiative Transfer Model-Neural Network ([IRTM-NN](https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-3-olci/level-2/imt-neural-net)). 

OLCI data from 2016 to 2021 concur with the production of the weekly climatology, which is then used as reference for the analysis. 
Daily time series of both OC (i.e., CHL and TSM) products are turned into weekly time series by averaging on a pixel-by-pixel basis. For each pixel the average and standard deviation is computed from a data cube of 3 pixels x 3 pixels x 7 days. This averaging reduces the impact of possible noise, common at these small scales, and increases spatial coverage mined by lack of data mostly due to clouds. Finally, we consider the difference between the “present” weekly observations and the weekly climatology at the scale of the pixel. This difference was judged against the climatology in order to obtain a relative, dimensionless value.



### The impacts of COVID-19 on water quality
The water quality analysis focuses on assessing the effect of the lockdown and the subsequent economic recovery on inland and coastal water quality by monitoring the deviation from a climatological mean of Chlorophyll-a concentration over a number of key Areas of Interest. 

In accordance with the weekly mean anomaly maps of Chl concentration, the time series shows after the lockdown date (March, 11th) predominant presence of days recording good water quality (green dots) and, in particular, a total absence of red dots. After the post-lockdown date (May, 4th) regular and low water quality (i.e., presence of blue and red dots) are recorded. This observation actually matches with the reactivation of some socio-economic activities within the investigated area. These anomalously low values indicate a water with lower amounts of Chl, compared to what is usually observed at this time of the year. A more in-depth analysis showed that they result from the cumulated impact of a number of natural phenomena. In particular, low wind magnitudes (top plot of Figure 1) were recorded at the AAOT from 5th to 20th April, which, by preserving the vertical stratification of the water column, hindered upwelling of nutrient-rich waters that may enhance the growth of phytoplankton. Such hypothesis is confirmed by significant increase of SST (bottom plot of Figure 1), as measured by a multi-sensor product (including data from NOAA-18, MetOpA-B, Aqua, Terra, MSG1, NPP, Meteosat11, Sentinel 3A-B) at the AAOT  during that period.

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/N3_regional_water_quality_timeseries/N3-Fig1.png)

*Figure 1: Chl-a concentration in the North Adriatic Sea during the Italian lockdown from OLCI (See Methods); the black line indicates the 2017–2019 climatologic values of Chl-a concentration; the grey shadow indicates the standard deviation; dots represent the weekly means of Chl-a concentration (green) below the climatologic value, (blue) above the climatologic value and below the standard deviation, (red) above the climatologic value and above the standard deviation; the red shaded area indicates the 2020 Italian lockdown.*

On top of this particular local conditions, water level data of Po River at Pontelagoscuro station (\~50 km upstream the river mouth) show that the lowest values of Chl concentration anomalies occur during the minimum of the Po River water discharge, recorded mid April 2020 (bottom panel of Figure 2), which indicates a reduced input of cold waters from the Po River tributaries debouching in the North Adriatic basin. The particularly warm bulge and the associated SST pattern along the north-west coast of the basin mark a reduction of the well-known cold coastal current that constitute the natural conveyor belt of the North Adriatic river plumes, i.e., the primary source of nutrient and sediment loads that flow southward.

Finally, we cannot exclude **a mutual role of a decrease of human activities that enhanced the negative anomaly in Chl concentration** as highlighted by the low turbidity values in the Po river measured by Sentinel-2 in the lockdown phase (top panel of Figure 2)

![](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/N3_regional_water_quality_timeseries/N3-Fig2.png)

*Figure 2: (Top) S2-derived turbidity maps in the last inland branch of the Po River March, 19th 2020 (beginning of lockdown) and April, 8th (middle of lockdown), (Bottom) Time series of the Po river water discharge at Pontelagoscuro station.*

###### Read more

Federica Braga, Daniele Ciani, Simone Colella, Emanuele Organelli, Jaime Pitarch, Vittorio E. Brando, Mariano Bresciani, Javier A. Concha, Claudia Giardino, Gian Marco Scarpa, Gianluca Volpe, Marie-Hélène Rio, Federico Falcini,
*COVID-19 lockdown effects on a coastal marine environment: Disentangling perception versus reality*,**Science of The Total Environment**,
Volume 817, 2022, 153002, ISSN 0048-9697, https://doi.org/10.1016/j.scitotenv.2022.153002, https://www.sciencedirect.com/science/article/pii/S0048969722000912
