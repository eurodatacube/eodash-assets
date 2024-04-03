## Ship Density Maps (Sentinel-1)

This indicator shows ships detected in the major EU ports by means of Copernicus Sentinel-1 data. It was developed by Alessandro Cimbelli within the upscaling part of the [RACE Challenges 2021](https://eo4society.esa.int/2021/08/01/rapid-action-on-coronavirus-and-eo-race-dashboard-challenge-3/).

A vessel density map is produced by deriving, for each 1 km2 pixel of the masked image of the selected area, an index given by the ratio:

density_vessels= 1000 * number_vessels / number_observations

where the number of observations corresponds to the intersection of all the satellite footprints of the selected month.

The figures below show a comparison with the corresponding map provided by [EMODnet](https://race.esa.int/?x=1040481.31544&y=5968190.74701&z=4.29471&poi=World-E13o&search=World%3A+Vessel+density+%28all%29+%5Bh%2Fsqkm%5D) using the Structural Similarity Index (SSIM).


<div style="display: flex;">
  <div class="image-caption-object">
      <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E1b_vessel_density_timeseries/E1b-img1.png" alt="Image" style="width: 40%;" />
      <div>Sentinel-1 based indicator</div>
  </div>
  
  <div class="image-caption-object">
      <img src="https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/E1b_vessel_density_timeseries/E1b-img2.png" alt="Legend" style="width: 40%;" />
      <div>EMODnet indicator</div>
  </div>
</div>


