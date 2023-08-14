//VERSION=3
function setup() {
    return {
      input: [{
        bands: [
          "tropno2",
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
    return {
      data:  [samples.tropno2],
      dataMask: [samples.dataMask]
    }
  }