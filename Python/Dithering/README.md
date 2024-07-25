# Floyd-Steinberg Dithering Algorithm

## Function Description

The `floyd_steinberg_dithering` function applies the Floyd-Steinberg dithering algorithm to a grayscale image. It takes either a PIL Image object or a numpy array as input and returns a dithered black and white image as a PIL Image object.

Key features:
- Converts grayscale images to black and white
- Uses error diffusion to create the illusion of more shades
- Handles both PIL Images and numpy arrays as input
- Includes type checking and error handling

## Understanding Dithering

### What is Dithering?

Dithering is a technique used in computer graphics to create the illusion of color depth in images with a limited color palette. It's particularly useful when converting images to a lower color depth, such as from grayscale to black and white.

### How Dithering Works

1. **Pixel Processing**: The algorithm processes each pixel in the image, usually from left to right and top to bottom.

2. **Thresholding**: Each pixel is compared to a threshold (often the midpoint between black and white). Pixels above the threshold become white, those below become black.

3. **Error Calculation**: The difference between the original pixel value and the new black or white value is calculated. This difference is called the "error".

4. **Error Diffusion**: The error is distributed to neighboring pixels that haven't been processed yet. This distribution follows a specific pattern:

   ```
   X   7/16
   3/16 5/16 1/16
   ```

   Where X is the current pixel, and the fractions show how the error is distributed to the neighboring pixels.

5. **Repetition**: This process is repeated for each pixel in the image.

### Quantitative Analysis of the Algorithm

Let's dive deeper into the mathematics behind the Floyd-Steinberg dithering algorithm:

1. **Thresholding**:
   For each pixel $(x, y)$, we apply the following operation:

$$new_{pixel} (x, y) = \begin{cases}
  1 & \text{if } old_{pixel}(x, y) \geq 0.5 \\
  0 & \text{if } old_{pixel}(x, y) < 0.5 
  \end{cases}$$

   Where 1 represents white and 0 represents black.

2. **Error Calculation**:
   The quantization error is calculated as:

$$error(x, y) = old_{pixel}(x, y) - new_{pixel}(x, y)$$

3. **Error Diffusion**:
   The error is then distributed to the neighboring pixels according to the Floyd-Steinberg filter:

$$\begin{aligned}
    pixel(x+1, y) &= pixel(x+1, y) + error(x, y) \times \frac{7}{16} \\
    pixel(x-1, y+1) &= pixel(x-1, y+1) + error(x, y) \times \frac{3}{16} \\
    pixel(x, y+1) &= pixel(x, y+1) + error(x, y) \times \frac{5}{16} \\
    pixel(x+1, y+1) &= pixel(x+1, y+1) + error(x, y) \times \frac{1}{16}
  \end{aligned}$$

5. **Accumulated Error**:
   Over time, the total accumulated error $E$ for the entire image can be expressed as:

$$E = \sum_{x=0}^{width-1} \sum_{y=0}^{height-1} |old_{pixel}(x, y) - new_{pixel}(x, y)|$$

   The goal of the algorithm is to minimize this accumulated error while still producing a binary (black and white) image.

6. **Perceptual Model**:
   The effectiveness of dithering relies on the human visual system's tendency to average intensities over small spatial regions. This can be modeled as a convolution with a Gaussian kernel:

   $perceived_{image} = dithered_{image} * G_{\sigma}$

   Where $G_{\sigma}$ is a 2D Gaussian function with standard deviation $\sigma$, and $*$ denotes convolution.


### Benefits of Dithering

- **Improved Perceived Quality**: Dithering can make an image appear to have more shades than it actually does, improving its perceived quality.
- **Reduced File Size**: It allows for the use of fewer colors while maintaining a semblance of the original image quality, which can lead to smaller file sizes.
- **Compatibility**: Useful for displays or printers with limited color capabilities.

### Applications

Dithering is commonly used in:
- Image processing software
- Printing technology
- Video game graphics (especially for older or limited-color systems)
- Digital audio (to reduce quantization noise)

By applying dithering, we can create visually appealing black and white images that retain much of the detail and gradients of the original grayscale images.
