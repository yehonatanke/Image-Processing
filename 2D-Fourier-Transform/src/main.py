import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from mpl_toolkits.mplot3d import Axes3D
from numpy.fft import fft2, ifft2, fftshift, ifftshift

from src.second_demo import second_demonstrate
from src.third_demo import third_demonstration


def create_image(size=128):
    """Create a simple image using sine and cosine functions."""
    x = np.linspace(-1, 1, size)
    y = np.linspace(-1, 1, size)
    xx, yy = np.meshgrid(x, y)
    image = np.sin(5 * xx) * np.cos(5 * yy)
    return image


def fourier_transform_2d(image):
    """Perform 2D Fourier Transform."""
    return fftpack.fft2(image)


def inverse_fourier_transform_2d(f_transform):
    """Perform Inverse 2D Fourier Transform."""
    return fftpack.ifft2(f_transform).real


def shift_spectrum(f_transform):
    """Shift the zero frequency component to the center of the spectrum."""
    return fftpack.fftshift(f_transform)


def magnitude_spectrum(f_transform):
    """Calculate the magnitude spectrum."""
    return np.log(np.abs(f_transform) + 1)


def phase_spectrum(f_transform):
    """Calculate the phase spectrum."""
    return np.angle(f_transform)


def plot_3d_surface(data, title):
    """Plot a 3D surface."""
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(0, data.shape[0])
    y = np.arange(0, data.shape[1])
    X, Y = np.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, data, cmap='viridis')
    ax.set_title(title)
    fig.colorbar(surf)


def demonstrate_2d_fourier_transform():
    # Create the image
    image = create_image()

    # Perform 2D Fourier Transform
    f_transform = fourier_transform_2d(image)

    # Shift the spectrum
    f_transform_shifted = shift_spectrum(f_transform)

    # Calculate magnitude and phase spectra
    magnitude_spectrum_result = magnitude_spectrum(f_transform_shifted)
    phase_spectrum_result = phase_spectrum(f_transform_shifted)

    # Perform inverse Fourier Transform
    reconstructed_image = inverse_fourier_transform_2d(f_transform)

    # Plot the results
    plt.figure(figsize=(20, 15))

    plt.subplot(231)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(232)
    plt.imshow(magnitude_spectrum_result, cmap='viridis')
    plt.title('Magnitude Spectrum')
    plt.axis('off')

    plt.subplot(233)
    plt.imshow(phase_spectrum_result, cmap='hsv')
    plt.title('Phase Spectrum')
    plt.axis('off')

    plt.subplot(234)
    plt.imshow(reconstructed_image, cmap='gray')
    plt.title('Reconstructed Image')
    plt.axis('off')

    plt.subplot(235)
    error = np.abs(image - reconstructed_image)
    plt.imshow(error, cmap='hot')
    plt.title('Reconstruction Error')
    plt.axis('off')

    plt.subplot(236)
    plt.hist(image.ravel(), bins=50, density=True, alpha=0.7, color='b')
    plt.hist(reconstructed_image.ravel(), bins=50, density=True, alpha=0.7, color='r')
    plt.title('Pixel Intensity Distribution')
    plt.legend(['Original', 'Reconstructed'])

    plt.tight_layout()
    plt.show()

    # 3D surface plots
    plot_3d_surface(image, 'Original Image - 3D Surface')
    plot_3d_surface(magnitude_spectrum_result, 'Magnitude Spectrum - 3D Surface')
    plot_3d_surface(phase_spectrum_result, 'Phase Spectrum - 3D Surface')

    plt.show()


# Run the demonstration
# demonstrate_2d_fourier_transform()
# second_demonstrate()
# third_demonstration()
fourth_demonstration()