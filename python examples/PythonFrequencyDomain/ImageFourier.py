# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 14:00:24 2015

@author: azariac
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('kidface.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()