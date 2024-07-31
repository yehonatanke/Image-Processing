# Fourier Transformations (Mathematical Summary)

## 1. Fourier Series

For a periodic function $f(x)$ with period $T$, the Fourier series representation is:

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[a_n \cos\left(\frac{2\pi nx}{T}\right) + b_n \sin\left(\frac{2\pi nx}{T}\right)\right]
$$

Where the coefficients are given by:

$$
\begin{align*}
a_0 &= \frac{2}{T} \int_{-T/2}^{T/2} f(x) dx \\
a_n &= \frac{2}{T} \int_{-T/2}^{T/2} f(x) \cos\left(\frac{2\pi nx}{T}\right) dx \\
b_n &= \frac{2}{T} \int_{-T/2}^{T/2} f(x) \sin\left(\frac{2\pi nx}{T}\right) dx
\end{align*}
$$

Explanation: The Fourier series decomposes a periodic function into a sum of simple oscillating functions (sines and cosines).

## 2. Fourier Transform

For a non-periodic function $f(x)$, the Fourier transform is defined as:

$$
F(\omega) = \int_{-\infty}^{\infty} f(x) e^{-i\omega x} dx
$$

And the inverse Fourier transform:

$$
f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i\omega x} d\omega
$$

Explanation: The Fourier transform extends the concept of Fourier series to non-periodic functions, representing them as a continuous spectrum of frequencies.

## 3. Properties of Fourier Transforms

### Linearity
$$
\mathcal{F}\{af(x) + bg(x)\} = aF(\omega) + bG(\omega)
$$

### Time Shifting
$$
\mathcal{F}\{f(x-a)\} = e^{-i\omega a}F(\omega)
$$

### Frequency Shifting
$$
\mathcal{F}\{e^{i\omega_0 x}f(x)\} = F(\omega - \omega_0)
$$

### Scaling
$$
\mathcal{F}\{f(ax)\} = \frac{1}{|a|}F\left(\frac{\omega}{a}\right)
$$

### Convolution Theorem
$$
\mathcal{F}\{f(x) * g(x)\} = F(\omega)G(\omega)
$$

Explanation: These properties make Fourier transforms powerful tools for analyzing and manipulating signals in various domains.

## 4. Discrete Fourier Transform (DFT)

For a discrete sequence $x[n]$ of length $N$, the DFT is:

$$
X[k] = \sum_{n=0}^{N-1} x[n] e^{-i2\pi kn/N}, \quad k = 0, 1, ..., N-1
$$

And the inverse DFT:

$$
x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{i2\pi kn/N}, \quad n = 0, 1, ..., N-1
$$

Explanation: The DFT is used for digital signal processing and is the basis for the Fast Fourier Transform (FFT) algorithm.

# Application to Image Processing

Now, let's connect this to image processing:

## 1. 2D Fourier Transform

For a 2D image $f(x,y)$ of size $M \times N$, the 2D DFT is:

$$
F(u,v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{-i2\pi(ux/M + vy/N)}
$$

Explanation: This extends the 1D DFT to 2D, allowing us to analyze images in the frequency domain.

## 2. Image Processing Applications

### a) Filtering
Low-pass filter (image smoothing):

$$H_{LP}(u,v) = \begin{cases} 
1 & \text{if } \sqrt{u^2 + v^2} \leq D_0 \\
0 & \text{otherwise}
\end{cases}$$

High-pass filter (edge detection):

$$H_{HP}(u,v) = 1 - H_{LP}(u,v)$$

### b) Image Compression
By discarding high-frequency components:

$$F'(u,v) = \begin{cases}
F(u,v) & \text{if } (u,v) \in \text{low frequency region} \\
0 & \text{otherwise}
\end{cases}$$

### c) Noise Removal
For periodic noise at frequency $(u_0, v_0)$:

$$H(u,v) = \begin{cases}
0 & \text{if } (u,v) = (u_0, v_0) \\
1 & \text{otherwise}
\end{cases}$$

Explanation: These applications leverage the frequency domain representation of images to perform various processing tasks efficiently.
