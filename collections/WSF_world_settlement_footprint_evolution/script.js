//VERSION=3
function setup() {
    return {
      input: [{
        bands: [
          "WSFevolution",
        ]
      }],
      output: [
        {
          id: "data",
          bands: 1,
          sampleType: "UINT16"
        }
      ]
    }
  }
  function evaluatePixel(samples) {
    return {
      data: [samples.WSFevolution],
    }
  }
