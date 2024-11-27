## Water Quality Regional Maps: Total suspended Matter

Total Suspended Matter (TSM) i.e, the concentration of organic and inorganic materials suspended in the water, is another proxy for water quality as different contaminants, including nutrients, trace metals, semi-volatile organic compounds, and numerous pesticides, can aggregate to these solids and brought in suspension. This can alter the state of the aquatic ecosystem and the use of freshwater resources. For instance, excessive suspended material might condition primary productivity. TSM concentration can be very high near the coasts due to the resuspension of terrestrial or submarine particulate matter by tides, waves, and currents.

### Dataset algorithm developemnt
- TSM data are specifically produced by CNR-ISMAR-GOS for the ESA-RACE Dashboard starting from Sentinel3-OLCI L2 data distributed by EUMETSAT (https://data.eumetsat.int) OLCI data from 2016 concur with the production of the weekly climatology, which is then used as reference for the analysis. 
- Daily time series  products are turned into weekly time series by averaging on a pixel-by-pixel basis:
  -  For each pixel the average and standard deviation is computed from a data cube of 3 pixels x 3 pixels x 7 days.
  -  This averaging reduces the impact of possible noise, common at these small scales, and increases spatial coverage mined by lack of data mostly due to clouds.
  -  Finally, it's considered the difference between the “present” weekly observations and the weekly climatology at the scale of the pixel. This difference was judged against the climatology in order to obtain a relative, dimensionless value.
