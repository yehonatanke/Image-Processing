# MATLAB Cheatsheet

## Table of Contents

### MATLAB Basics
1. [Basic Operations](#basic-operations)
   - [Arithmetic Operations](#arithmetic-operations)
   - [Logical Operations](#logical-operations)
   - [Variable Assignment](#variable-assignment)
2. [Data Types](#data-types)
   - [Numeric Types](#numeric-types)
   - [Strings and Characters](#strings-and-characters)
   - [Logical](#logical)
   - [Cell Arrays](#cell-arrays)
   - [Structures](#structures)
3. [Arrays and Matrices](#arrays-and-matrices)
   - [Creating Arrays](#creating-arrays)
   - [Special Matrices](#special-matrices)
   - [Array Operations](#array-operations)
4. [Control Structures](#control-structures)
   - [If-Else Statement](#if-else-statement)
   - [For Loop](#for-loop)
   - [While Loop](#while-loop)
   - [Switch Statement](#switch-statement)
5. [Functions](#functions)
   - [Function Definition](#function-definition)
   - [Anonymous Functions](#anonymous-functions)
6. [Plotting](#plotting)
   - [2D Plots](#2d-plots)
   - [3D Plots](#3d-plots)
7. [File I/O](#file-io)
   - [Reading Data](#reading-data)
   - [Writing Data](#writing-data)
8. [Debugging](#debugging)

### Image Processing
1. [Reading and Writing Images](#reading-and-writing-images)
2. [Basic Image Information](#basic-image-information)
3. [Image Manipulation](#image-manipulation)
4. [Color Space Conversions](#color-space-conversions)
5. [Filtering and Enhancement](#filtering-and-enhancement)
6. [Edge Detection](#edge-detection)
7. [Morphological Operations](#morphological-operations)
8. [Segmentation](#segmentation)
9. [Feature Extraction](#feature-extraction)
10. [Frequency Domain Processing](#frequency-domain-processing)
11. [Image Analysis](#image-analysis)
12. [Thresholding](#thresholding)
    - [Basic Thresholding](#basic-thresholding)
    - [Advanced Thresholding Techniques](#advanced-thresholding-techniques)
13. [Advanced Image Manipulations](#advanced-image-manipulations)
    - [Intensity Adjustment](#intensity-adjustment)
    - [Histogram Equalization](#histogram-equalization)
    - [Image Sharpening](#image-sharpening)
    - [Image Denoising](#image-denoising)
    - [Active Contours](#active-contours)
    - [Intensity-based Segmentation](#intensity-based-segmentation)
    - [Morphological Operations](#morphological-operations-1)
    - [Image Registration](#image-registration)
    - [Image Fusion](#image-fusion)
    - [Color-based Segmentation](#color-based-segmentation)
   

## Basic Operations

### Arithmetic Operations
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Power: `^`
- Element-wise operations: `.* ./ .^`

### Logical Operations
- Equal to: `==`
- Not equal to: `~=`
- Greater than: `>`
- Less than: `<`
- Greater than or equal to: `>=`
- Less than or equal to: `<=`
- AND: `&&`
- OR: `||`
- NOT: `~`

### Variable Assignment
```matlab
x = 5;  % Assign value 5 to x
y = 'Hello';  % Assign string 'Hello' to y
```

## Data Types

### Numeric Types
- Double: `x = 3.14`
- Integer: `x = int32(5)`
- Complex: `x = 3 + 4i`

### Strings and Characters
- String: `str = "Hello, World!"`
- Character array: `chr = 'Hello'`

### Logical
- Boolean: `flag = true`

### Cell Arrays
```matlab
cell_array = {1, 'text', [1 2 3]}
```

### Structures
```matlab
student.name = 'John';
student.age = 20;
student.grades = [85, 90, 78];
```

## Arrays and Matrices

### Creating Arrays
```matlab
a = [1 2 3 4];  % Row vector
b = [1; 2; 3; 4];  % Column vector
C = [1 2 3; 4 5 6; 7 8 9];  % 3x3 matrix
```

### Special Matrices
```matlab
zeros(3)  % 3x3 matrix of zeros
ones(2,3)  % 2x3 matrix of ones
eye(4)  % 4x4 identity matrix
rand(2,2)  % 2x2 matrix of random numbers
```

### Array Operations
```matlab
size(A)  % Size of array A
length(v)  % Length of vector v
A'  % Transpose of A
inv(A)  % Inverse of A
det(A)  % Determinant of A
eig(A)  % Eigenvalues and eigenvectors of A
```

## Control Structures

### If-Else Statement
```matlab
if condition
    % code
elseif another_condition
    % code
else
    % code
end
```

### For Loop
```matlab
for i = 1:10
    % code
end
```

### While Loop
```matlab
while condition
    % code
end
```

### Switch Statement
```matlab
switch variable
    case value1
        % code
    case value2
        % code
    otherwise
        % code
end
```

## Functions

### Function Definition
```matlab
function [output1, output2] = functionName(input1, input2)
    % Function body
end
```

### Anonymous Functions
```matlab
f = @(x) x^2 + 2*x + 1;
```

## Plotting

### 2D Plots
```matlab
x = 0:0.1:2*pi;
y = sin(x);
plot(x, y)
title('Sin Function')
xlabel('x')
ylabel('sin(x)')
grid on
```

### 3D Plots
```matlab
[X, Y] = meshgrid(-2:0.2:2);
Z = X.^2 + Y.^2;
surf(X, Y, Z)
```

## File I/O

### Reading Data
```matlab
data = load('filename.mat');
txt_data = readtable('filename.txt');
csv_data = csvread('filename.csv');
```

### Writing Data
```matlab
save('filename.mat', 'variable1', 'variable2');
writetable(table_data, 'filename.txt');
csvwrite('filename.csv', matrix_data);
```

## Debugging

- `keyboard`: Pause execution and enter debug mode
- `dbstop`: Set breakpoint
- `dbclear`: Clear breakpoint
- `dbcont`: Continue execution
- `dbstep`: Step to next line
- `dbquit`: Quit debug mode

# Image Processing Cheatsheet

## Reading and Writing Images

```matlab
% Read an image
img = imread('filename.jpg');

% Write an image
imwrite(img, 'output.jpg');

% Display an image
imshow(img);
```

## Basic Image Information

```matlab
% Get image size
[height, width, channels] = size(img);

% Get image type
class(img)

% Convert image type
img_double = im2double(img);
img_uint8 = im2uint8(img);
```

## Image Manipulation

```matlab
% Crop image
cropped_img = imcrop(img, [x y width height]);

% Resize image
resized_img = imresize(img, scale);
resized_img = imresize(img, [new_height new_width]);

% Rotate image
rotated_img = imrotate(img, angle);

% Flip image
flipped_horizontal = fliplr(img);
flipped_vertical = flipud(img);
```

## Color Space Conversions

```matlab
% RGB to Grayscale
gray_img = rgb2gray(rgb_img);

% RGB to HSV
hsv_img = rgb2hsv(rgb_img);

% Grayscale to Binary
binary_img = imbinarize(gray_img);
```

## Filtering and Enhancement

```matlab
% Apply Gaussian filter
blurred_img = imgaussfilt(img, sigma);

% Median filter
filtered_img = medfilt2(img);

% Adjust contrast
enhanced_img = imadjust(img);

% Sharpen image
sharpened_img = imsharpen(img);
```

## Edge Detection

```matlab
% Canny edge detection
edges = edge(gray_img, 'Canny');

% Sobel edge detection
edges_sobel = edge(gray_img, 'Sobel');
```

## Morphological Operations

```matlab
% Dilation
dilated_img = imdilate(binary_img, strel('disk', radius));

% Erosion
eroded_img = imerode(binary_img, strel('disk', radius));

% Opening (erosion followed by dilation)
opened_img = imopen(binary_img, strel('disk', radius));

% Closing (dilation followed by erosion)
closed_img = imclose(binary_img, strel('disk', radius));
```

## Segmentation

```matlab
% Otsu's method for thresholding
level = graythresh(gray_img);
binary_img = imbinarize(gray_img, level);

% K-means clustering
[segmented_img, centers] = imsegkmeans(img, k);
```

## Feature Extraction

```matlab
% Detect SURF features
points = detectSURFFeatures(gray_img);

% Extract HOG features
[features, visualization] = extractHOGFeatures(gray_img);
```

## Frequency Domain Processing

```matlab
% Fourier Transform
F = fft2(gray_img);
F_shifted = fftshift(F);

% Inverse Fourier Transform
restored_img = ifft2(ifftshift(F_shifted));
```

## Image Analysis

```matlab
% Histogram
imhist(gray_img);

% Find connected components
cc = bwconncomp(binary_img);

% Measure region properties
stats = regionprops(cc, 'Area', 'Centroid');
```

## Basic Thresholding

### Basic Thresholding

```matlab
% Read an image
im2 = imread('pic1.jpg');

% Create and display a binary image
% Pixels > 128 become white (1), others become black (0)
imshow(im2 > 128);

% For color images, apply to a single channel (e.g., red channel)
imshow(im2(:,:,1) > 128);

% Or convert to grayscale first
gray_im2 = rgb2gray(im2);
imshow(gray_im2 > 128);
```

This technique is useful for basic image segmentation or creating masks of brighter areas in an image. For color images, consider applying it to individual channels or converting to grayscale first for more predictable results.

### Advanced Thresholding Techniques

```matlab
% Otsu's method for automatic thresholding
gray_img = rgb2gray(img);
level = graythresh(gray_img);
BW = imbinarize(gray_img, level);
imshow(BW);

% Adaptive thresholding
BW = imbinarize(gray_img, 'adaptive', 'ForegroundPolarity', 'dark', 'Sensitivity', 0.4);
imshow(BW);

% Multi-level thresholding
levels = multithresh(gray_img, 3);  % 3 thresholds
seg_img = imquantize(gray_img, levels);
imshow(seg_img, []);

% Hysteresis thresholding (often used with edge detection)
BW = edge(gray_img, 'Canny');
imshow(BW);
```

## Image Manipulations

```matlab
% Adjust image intensity values
adjusted = imadjust(img, [low_in high_in], [low_out high_out]);

% Histogram equalization
eq_img = histeq(gray_img);

% Contrast-limited adaptive histogram equalization (CLAHE)
eq_img = adapthisteq(gray_img);

% Image sharpening
sharp_img = imsharpen(img, 'Radius', 2, 'Amount', 1);

% Image denoising
denoised = imgaussfilt(img, 2);  % Gaussian filter
denoised = medfilt2(img);  % Median filter

% Image segmentation using active contours
mask = false(size(gray_img));
mask(25:end-25, 25:end-25) = true;
BW = activecontour(gray_img, mask, 200);

% Intensity-based segmentation
[~, threshold] = edge(gray_img, 'sobel');
fudgeFactor = 0.5;
BW = edge(gray_img, 'sobel', threshold * fudgeFactor);

% Morphological operations
se = strel('disk', 5);
dilated = imdilate(BW, se);
eroded = imerode(BW, se);
opened = imopen(BW, se);
closed = imclose(BW, se);

% Image registration (aligning images)
[optimizer, metric] = imregconfig('multimodal');
movingRegistered = imregister(moving, fixed, 'affine', optimizer, metric);

% Image fusion
fused = imfuse(img1, img2, 'blend', 'Scaling', 'joint');

% Color-based segmentation
lab_img = rgb2lab(img);
ab = lab_img(:,:,2:3);
ab = im2single(ab);
nColors = 3;
pixel_labels = imsegkmeans(ab, nColors, 'NumAttempts', 3);
```
