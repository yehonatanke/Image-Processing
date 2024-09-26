import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft2, ifft2, fftshift, ifftshift


# Create a simple 2D signal (image) - a checkerboard pattern
def create_checkerboard(n, m):
    re = np.r_[n * [0, 1]]  # alternate 0s and 1s n times
    checkerboard = np.row_stack(m * (re, re[::-1]))
    return checkerboard


def second_demonstrate():
    # Generate a 2D checkerboard pattern of size 8x8
    image = create_checkerboard(8, 8)

    # Compute the 2D Fourier Transform of the image
    f_transform = fft2(image)

    # Shift the zero frequency component to the center of the spectrum
    f_transform_shifted = fftshift(f_transform)

    # Compute the magnitude spectrum
    magnitude_spectrum = np.abs(f_transform_shifted)

    # Perform the inverse Fourier Transform to convert back to spatial domain
    f_ishift = ifftshift(f_transform_shifted)  # undo fftshift
    image_reconstructed = ifft2(f_ishift).real  # inverse FFT and take real part

    # Plot the original image, Fourier Transform, and reconstructed image
    plt.figure(figsize=(12, 8))

    # Original Image
    plt.subplot(2, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    # Fourier Transform (Complex Values)
    plt.subplot(2, 3, 2)
    plt.imshow(np.log(1 + np.abs(f_transform)), cmap='gray')
    plt.title('Fourier Transform (Raw)')
    plt.axis('off')

    # Fourier Transform (Shifted)
    plt.subplot(2, 3, 3)
    plt.imshow(np.log(1 + magnitude_spectrum), cmap='gray')
    plt.title('Shifted Fourier Transform')
    plt.axis('off')

    # Real Part of Fourier Transform
    plt.subplot(2, 3, 4)
    plt.imshow(np.real(f_transform_shifted), cmap='gray')
    plt.title('Real Part of Fourier Transform')
    plt.axis('off')

    # Imaginary Part of Fourier Transform
    plt.subplot(2, 3, 5)
    plt.imshow(np.imag(f_transform_shifted), cmap='gray')
    plt.title('Imaginary Part of Fourier Transform')
    plt.axis('off')

    # Reconstructed Image (after inverse FFT)
    plt.subplot(2, 3, 6)
    plt.imshow(image_reconstructed, cmap='gray')
    plt.title('Reconstructed Image (from FFT)')
    plt.axis('off')

    plt.tight_layout()
    plt.show()
