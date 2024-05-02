//VERSION=3
function setup() {
  return {
    input: [{
      bands: [
        "chl",
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
  if (samples.chl >= 2e3) {
    validValue = 0
  }
  let index = samples.chla;
  return {
    data: [index],
    dataMask: [samples.dataMask * validValue]
  }
}
