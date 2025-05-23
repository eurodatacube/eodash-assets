//VERSION=3
function setup() {
  return {
    input: [{
      bands: [
        "WindU100m",
        "dataMask"
      ]
    }],
    output: [
      {
        id: "data",
        bands: 1,
        sampleType: "FLOAT32"
      },
      {
        id: "dataMask",
        bands: 1
      }
    ]
  }
}
function evaluatePixel(samples) {
  let validValue = 1
  // data sanitation
  if (samples.WindU100m >= 1e20) {
    validValue = 0
  }
  let index = samples.WindU100m;
  return {
    data: [index],
    dataMask: [samples.dataMask * validValue]
  }
}
