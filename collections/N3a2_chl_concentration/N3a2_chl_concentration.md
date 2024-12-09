## Water Quality Regional Maps: Chlorophyll-a (Chl-a) concentration

Chlorophyll-a (Chl-a) concentration is an indicator of algae abundance which fluctuates naturally over space and time, as a result of combined atmospheric and oceanic effects (e.g., marine currents and upwelling). In coastal areas, strongly influenced by river inputs and human activities, high Chl concentration can result from the discharge of urban sewage, industrial runoffs, and fertilizers from agriculture activities over watersheds. In particular, nutrient inputs of anthropogenic origin affect the natural amount of phytoplankton in marine and inland waters, representing a continuous threat to biodiversity and leading to undesirable modifications of phytoplankton concentration (i.e., eutrophication).

#### Dataset algorithm development
 - Daily time series of Chl-a products are turned into weekly time series by averaging on a pixel-by-pixel basis. For each pixel the average and standard deviation is computed from a data cube of 3 pixels x 3 pixels x 7 days.
 - This averaging reduces the impact of possible noise, common at these small scales, and increases spatial coverage mined by lack of data mostly due to clouds.
 - Finally, we consider the difference between the “present” weekly observations and the weekly climatology at the scale of the pixel. This difference was judged against the climatology in order to obtain a relative, dimensionless value.
