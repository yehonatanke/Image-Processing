# Fourier Transformation in Image Processing (with Formulas)

## Formulas

### 1. 2D Discrete Fourier Transform (DFT)

For an image $f(x,y)$ of size $M \times N$, the 2D DFT is given by:

$$
F(u,v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) \cdot e^{-j2\pi(\frac{ux}{M} + \frac{vy}{N})}
$$

Where:
- $F(u,v)$ is the Fourier transform
- $f(x,y)$ is the image in the spatial domain
- $e$ is the base of natural logarithms
- $j$ is the imaginary unit
- $x, y$ are spatial coordinates
- $u, v$ are frequency coordinates
- $M, N$ are image dimensions

### 2. Inverse 2D Discrete Fourier Transform (IDFT)

To convert back from the frequency domain to the spatial domain:

$$
f(x,y) = \frac{1}{MN} \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(u,v) \cdot e^{j2\pi(\frac{ux}{M} + \frac{vy}{N})}
$$

Where:
- $f(x,y)$ is the reconstructed image in the spatial domain
- $F(u,v)$ is the image in the frequency domain

### 3. Fourier Transform Properties

#### Linearity

$$
\mathcal{F}\{af_1(x,y) + bf_2(x,y)\} = aF_1(u,v) + bF_2(u,v)
$$

#### Translation

$$
\mathcal{F}\{f(x-x_0, y-y_0)\} = F(u,v)e^{-j2\pi(\frac{ux_0}{M} + \frac{vy_0}{N})}
$$

#### Rotation

If $f'(x,y)$ is $f(x,y)$ rotated by an angle $\theta$, then:

$$
F'(u,v) = F(u \cos \theta + v \sin \theta, -u \sin \theta + v \cos \theta)
$$

### 4. Frequency Domain Filtering

A general form of frequency domain filtering:

$$
G(u,v) = H(u,v) \cdot F(u,v)
$$

Where:
- $G(u,v)$ is the filtered image in the frequency domain
- $H(u,v)$ is the filter transfer function
- $F(u,v)$ is the Fourier transform of the original image

