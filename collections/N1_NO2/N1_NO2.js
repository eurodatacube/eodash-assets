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
    let validValue = 1
    // data sanitation
    if (samples.tropno2 >= 1e20 ){
        validValue = 0
    }
    let index = samples.tropno2;
    return {
      data:  [index],
      dataMask: [samples.dataMask * validValue]
    }
  }
