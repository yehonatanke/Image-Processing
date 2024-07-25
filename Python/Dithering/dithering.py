from typing import Union
import numpy as np
from PIL import Image


def floyd_steinberg_dithering(image: Union[Image.Image, np.ndarray]) -> Image.Image:
    """
    Applies Floyd-Steinberg dithering to a grayscale image.
    
    This function implements the Floyd-Steinberg dithering algorithm,
    which is an error diffusion method that creates the illusion of
    color depth in images with a limited color palette.
    
    Args:
    image (Union[PIL.Image.Image, np.ndarray]): A grayscale input image, 
        either as a PIL Image or a numpy array.
    
    Returns:
    PIL.Image.Image: The dithered black and white image.
    
    Raises:
    ValueError: If the input is not a 2D grayscale image.
    """
    # Convert image to numpy array if it's a PIL Image
    if isinstance(image, Image.Image):
        img_array = np.array(image, dtype=float) / 255
    elif isinstance(image, np.ndarray):
        img_array = image.astype(float) / 255
    else:
        raise ValueError("Input must be a PIL Image or numpy array")
    
    if img_array.ndim != 2:
        raise ValueError("Input must be a 2D grayscale image")
    
    height, width = img_array.shape
    
    for y in range(height):
        for x in range(width):
            old_pixel = img_array[y, x]
            new_pixel = np.round(old_pixel)
            img_array[y, x] = new_pixel
            error = old_pixel - new_pixel
            
            # Distribute the error to neighboring pixels
            if x + 1 < width:
                img_array[y, x + 1] += error * 7/16
            if x - 1 >= 0 and y + 1 < height:
                img_array[y + 1, x - 1] += error * 3/16
            if y + 1 < height:
                img_array[y + 1, x] += error * 5/16
            if x + 1 < width and y + 1 < height:
                img_array[y + 1, x + 1] += error * 1/16
    
    # Convert back to PIL Image
    return Image.fromarray((img_array * 255).astype(np.uint8))

def main() -> None:
    """
    Main function to demonstrate the usage of floyd_steinberg_dithering.
    """
    # Load a grayscale image
    input_image = Image.open('input_image.png').convert('L')

    # Perform dithering
    dithered_image = floyd_steinberg_dithering(input_image)

    # Save the result
    dithered_image.save('dithered_output.png')

if __name__ == "__main__":
    main()
