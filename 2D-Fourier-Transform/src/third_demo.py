import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack


def create_test_image(size=128):
    x = np.linspace(-1, 1, size)
    y = np.linspace(-1, 1, size)
    xx, yy = np.meshgrid(x, y)

    # Create a simple image with two Gaussian peaks
    image = np.exp(-5 * (xx ** 2 + yy ** 2)) + 0.5 * np.exp(-30 * ((xx - 0.5) ** 2 + (yy - 0.5) ** 2))

    return image


def plot_spectrum(fig, ax, data, title, xlabel, ylabel):
    im = ax.imshow(data, cmap='viridis')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.colorbar(im, ax=ax)


def apply_filter(f_transform, filter_func):
    rows, cols = f_transform.shape
    center_row, center_col = rows // 2, cols // 2
    y, x = np.ogrid[-center_row:rows - center_row, -center_col:cols - center_col]
    mask = filter_func(x, y)
    return f_transform * mask


def low_pass_filter(x, y, d=30):
    return x * x + y * y <= d * d


def high_pass_filter(x, y, d=30):
    return x * x + y * y > d * d


def third_demonstration():
    # Create a test image
    image = create_test_image()

    # Compute the 2D Fourier Transform
    f_transform = fftpack.fft2(image)
    f_transform_shifted = fftpack.fftshift(f_transform)

    # Compute magnitude and phase spectra
    magnitude_spectrum = np.abs(f_transform_shifted)
    log_magnitude_spectrum = np.log(1 + magnitude_spectrum)
    phase_spectrum = np.angle(f_transform_shifted)

    # Apply a low-pass filter
    filtered_f_transform = apply_filter(f_transform_shifted, low_pass_filter)
    filtered_image = np.real(fftpack.ifft2(fftpack.ifftshift(filtered_f_transform)))

    # Compute the Inverse Fourier Transform
    inverse_transform = np.real(fftpack.ifft2(f_transform))

    # Create subplots
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle("2D Fourier Transform Demonstration", fontsize=16)

    # Plot original image
    plot_spectrum(fig, axs[0, 0], image, "Original Image", "Pixel Position (Horizontal)", "Pixel Position (Vertical)")

    # Plot magnitude spectrum
    plot_spectrum(fig, axs[0, 1], magnitude_spectrum, "Magnitude Spectrum", "Frequency (Horizontal, cycles/pixel)",
                  "Frequency (Vertical, cycles/pixel)")

    # Plot log-transformed magnitude spectrum
    plot_spectrum(fig, axs[0, 2], log_magnitude_spectrum, "Log-Transformed Magnitude Spectrum", "Frequency (Horizontal, cycles/pixel)",
                  "Frequency (Vertical, cycles/pixel)")

    # Plot phase spectrum
    plot_spectrum(fig, axs[1, 0], phase_spectrum, "Phase Spectrum", "Frequency (Horizontal, cycles/pixel)", "Frequency (Vertical, cycles/pixel)")

    # Plot inverse Fourier transform (reconstructed image)
    plot_spectrum(fig, axs[1, 1], inverse_transform, "Inverse Fourier Transform", "Pixel Position (Horizontal)", "Pixel Position (Vertical)")

    # Plot filtered image
    plot_spectrum(fig, axs[1, 2], filtered_image, "Filtered Image (Low-Pass)", "Pixel Position (Horizontal)", "Pixel Position (Vertical)")

    plt.tight_layout()
    plt.show()


def create_square_image(size=64, square_size=16):
    image = np.zeros((size, size))
    center = size // 2
    start = center - square_size // 2
    end = start + square_size
    image[start:end, start:end] = 1.0
    return image


def fourth_demonstration():
    # Create a simple square image
    image = create_square_image()

    # Compute the 2D Fourier Transform
    f_transform = fftpack.fft2(image)
    f_transform_shifted = fftpack.fftshift(f_transform)

    # Compute magnitude and phase spectra
    magnitude_spectrum = np.abs(f_transform_shifted)
    log_magnitude_spectrum = np.log(1 + magnitude_spectrum)
    phase_spectrum = np.angle(f_transform_shifted)

    # Compute the Inverse Fourier Transform
    inverse_transform = np.real(fftpack.ifft2(f_transform))

    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 12))
    fig.suptitle("2D Fourier Transform of a Simple Square", fontsize=16)

    # Plot original image
    plot_spectrum(fig, axs[0, 0], image, "Original Image", "Pixel Position (Horizontal)", "Pixel Position (Vertical)")

    # Plot magnitude spectrum
    plot_spectrum(fig, axs[0, 1], magnitude_spectrum, "Magnitude Spectrum", "Frequency (Horizontal, cycles/pixel)",
                  "Frequency (Vertical, cycles/pixel)")

    # Plot log-transformed magnitude spectrum
    plot_spectrum(fig, axs[1, 0], log_magnitude_spectrum, "Log-Transformed Magnitude Spectrum", "Frequency (Horizontal, cycles/pixel)",
                  "Frequency (Vertical, cycles/pixel)")

    # Plot phase spectrum
    plot_spectrum(fig, axs[1, 1], phase_spectrum, "Phase Spectrum", "Frequency (Horizontal, cycles/pixel)", "Frequency (Vertical, cycles/pixel)")

    plt.tight_layout()
    plt.show()
