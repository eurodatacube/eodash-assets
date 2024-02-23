//VERSION=3
function setup() {
  return {
    input: [{
      bands: [
        "AIR2MT",
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
  if (samples.AIR2MT >= 1e20) {
    validValue = 0
  }
  let index = samples.AIR2MT;
  return {
    data: [index],
    dataMask: [samples.dataMask * validValue]
  }
}
