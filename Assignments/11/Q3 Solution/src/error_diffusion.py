import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def quantize(value, levels):
    """
    Find the closest available gray level for a given pixel value.

    :param value: The original pixel value
    :param levels: Array of available gray levels
    :return: The closest available gray level
    """
    return levels[np.argmin(np.abs(levels - value))]


def error_diffusion(image, m):
    """
    Perform error diffusion dithering on the input image.

    :param image: Input grayscale image as a 2D numpy array
    :param m: Number of gray levels to use
    :return: Dithered image as a 2D numpy array
    """
    # Define the available gray levels based on m
    levels = np.array([0, 64, 128, 192, 255])[:m]

    # Get image dimensions
    height, width = image.shape

    # Create output image, using float for precise error calculation
    output = np.zeros_like(image, dtype=float)

    # Iterate through each pixel in the image
    for y in range(height):
        for x in range(width):
            # Get the original pixel value
            old_pixel = image[y, x]

            # Find the closest available gray level
            new_pixel = quantize(old_pixel, levels)

            # Set the new pixel value in the output image
            output[y, x] = new_pixel

            # Calculate the quantization error
            error = old_pixel - new_pixel

            # Distribute the error to neighboring pixels (Floyd-Steinberg dithering)
            if x + 1 < width:
                output[y, x + 1] += error * 7 / 16
            if y + 1 < height:
                if x > 0:
                    output[y + 1, x - 1] += error * 3 / 16
                output[y + 1, x] += error * 5 / 16
                if x + 1 < width:
                    output[y + 1, x + 1] += error * 1 / 16

    # Convert the output back to uint8 (0-255 range)
    return output.astype(np.uint8)


def process_image(image_path: str, m: int, save_to_dir: bool = False) -> None:
    """
    Load an image, perform error diffusion, display results, and save output.

    :param image_path: Path to the input image file
    :param m: Number of gray levels to use
    :param save_to_dir: Whether to save the output image to directory
    """
    original = np.array(Image.open(image_path).convert('L'))

    # Perform error diffusion
    dithered = error_diffusion(original, m)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    setup_axes(ax1, original, 'Original')
    setup_axes(ax2, dithered, f'Dithered ({m} levels)')
    plt.tight_layout()
    plt.show()

    # Save the dithered image
    if save_to_dir:
        image_name = image_path.split('/')[-1].split('.')[0]
        output_directory = 'output'
        output_path = f'{output_directory}/{image_name}_dithered_{m}_levels.png'
        Image.fromarray(dithered).save(output_path)


def setup_axes(ax, img, title):
    x_ticks = np.linspace(0, img.shape[1] - 1, 5, dtype=int)
    y_ticks = np.linspace(0, img.shape[0] - 1, 5, dtype=int)
    tick_values = [0, 64, 128, 192, 255]
    ax.imshow(img, cmap='gray')
    ax.set_title(title)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)
    ax.set_xticklabels(tick_values)
    ax.set_yticklabels(tick_values)
    ax.set_xlim(0, img.shape[1] - 1)
    ax.set_ylim(img.shape[0] - 1, 0)