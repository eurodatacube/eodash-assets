//VERSION=3
function setup() {
  return {
    input: [{
      bands: [
        "OHC",
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
  let index = samples.OHC / 10e9;
  return {
    data: [index],
    dataMask: [samples.dataMask]
  }
}
