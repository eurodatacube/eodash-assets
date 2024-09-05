## CNN Model

U-Net has a near-symmetric encoder–decoder structure in which the contracting path captures rich low-level representations while the expanding path enables precise localization. Skip-connections are used between corresponding pairs of encoder and decoder blocks to propagate information from the contracting path to the expanding path. This facilitates the recovery of high-frequency spatial information and improves the boundary accuracy. In the U-Net architecture, a block constitutes a sequence of two 3×3 convolutional layers, each followed by a batch normalization (BN) procedure and the rectified linear unit (ReLU) activation function. In the contracting path, 2×2 max-pooling operations are used for feature map downsampling. Similarly, in the expanding path, every block is preceded by a bilinear upsampling operation. Each symmetric encoder and decoder block with a skip connection between them is defined here as a level. 
A schematic overview of a regular four-level U-Net architecture is shown in Fig. 1. The original U-Net in [1] uses the identical number of filters in the convolutional layers across the same level and doubles them for each level, i.e., 64, 128, 256, and 512. Here, we utilise 8 levels and limit the number of filters to 32 in the initial and final levels, and 64 in the other levels. The U-Net implementation is available at [2].


![Schematic overview of a four-level U-Net architecture](https://raw.githubusercontent.com/eurodatacube/eodash-assets/main/collections/Polartep_SeaIceDetection_tif_demo/model_schema.png "Schematic overview of a four-level U-Net architecture")


### References
[1] O. Ronneberger, P. Fischer and T. Brox, "U-Net: Convolutional networks for biomedical image segmentation", Proc. Int. Conf. Med. Image Comput. Comput.-Assist. Intervent., pp. 234-241, Oct. 2015.               
[2] A. Stokholm and A. Kucik, U-Net model PyTorch implementation, 2021, [online] Available: https://github.com/astokholm/AI4SeaIce.git.


