//VERSION=3
function setup() {
  return {
    input: ["LST", "dataMask"],
    mosaicking: Mosaicking.TILE,
    output: {
      bands: 4,
      sampleType: "UINT8"
    }
  };
}

function evaluatePixel(samples, scenes, inputMetadata, customData) {

  // Set min and max values dynamically
  const minValue = customData.minValue !== undefined ? customData.minValue : 250;
  const maxValue = customData.maxValue !== undefined ? customData.maxValue : 330;

  // Apply scale factor and offset
  const scaleFactor = 0.002;
  const offset = 290;

  for (let i = 0; i < samples.length; i++) {
    let sample = samples[i];
    
    // Apply the scale factor and offset to the LST value
    let val = sample.LST * scaleFactor + offset;

    // Color scale with smooth gradients for typical land surface temperature visualization
    let result = colorBlend(val, 
      [minValue, 
       minValue + (maxValue - minValue) * 0.1, 
       minValue + (maxValue - minValue) * 0.3, 
       minValue + (maxValue - minValue) * 0.5, 
       minValue + (maxValue - minValue) * 0.7, 
       minValue + (maxValue - minValue) * 0.9, 
       maxValue],
      [[255, 255, 255, 255],  // White (coldest)
       [173, 216, 230, 255],  // Light Blue
       [0, 0, 255, 255],      // Blue
       [255, 255, 0, 255],    // Yellow
       [255, 165, 0, 255],    // Orange
       [255, 69, 0, 255],     // Dark Orange
       [255, 0, 0, 255]]);    // Red (hottest)
    
    if (sample.dataMask == 1) {
      return result;
    }
  }
  return [0, 0, 0, 0];
}
