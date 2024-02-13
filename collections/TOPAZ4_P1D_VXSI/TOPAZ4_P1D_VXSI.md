# Arctic Ocean Physics Reanalysis

The current version of the TOPAZ system - TOPAZ4b - is nearly identical to the real-time forecast system run at MET Norway. It uses a recent version of the Hybrid Coordinate Ocean Model (HYCOM) developed at University of Miami (Bleck 2002). HYCOM is coupled to a sea ice model; ice thermodynamics are described in Drange and Simonsen (1996) and the elastic-viscous-plastic rheology in Hunke and Dukowicz (1997). The model's native grid covers the Arctic and North Atlantic Oceans, has fairly homogeneous horizontal spacing (between 11 and 16 km). 50 hybrid layers are used in the vertical (z-isopycnal), more than the TOPAZ4 system (28 layers). TOPAZ4b uses the Deterministic version of the Ensemble Kalman filter (DEnKF; Sakov and Oke 2008) to assimilate remotely sensed as well as temperature and salinity profiles. The output is interpolated onto standard grids and depths.

ARCTIC_MULTIYEAR_PHY_002_003 is the reanalysis product of the Arctic Monitoring and Forecasting
Center, and is composed of 3D, daily (monthly and yearly also) mean fields of temperature, salinity, sea
surface height, zonal velocity, meridional velocity, sea ice concentration, sea ice thickness and sea ice
velocity. 
