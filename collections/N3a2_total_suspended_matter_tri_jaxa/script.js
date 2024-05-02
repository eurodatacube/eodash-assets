//VERSION=3
function setup() {
  return {
    input: [{
      bands: [
        "tsmnn",
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
  if (samples.tsmnn >= 2e3) {
    validValue = 0
  }
  let index = samples.tsm;
  return {
    data: [index],
    dataMask: [samples.dataMask * validValue]
  }
}
