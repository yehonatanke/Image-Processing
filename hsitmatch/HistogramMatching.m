function  HistogramMatching
close all
A = imread('spine.jpg');
A = rgb2gray(A);
figure; imshow(A, []);
title('Original Image');
figure; imhist(A); title('source hist');


ref = imread('moon.jpg');
ref = rgb2gray(ref);
figure, imshow(ref, []);
title('Reference Image');
figure; imhist(ref); title('reference hist')

B = imhistmatch(A, ref);

figure, imshow(B, []);
title('Histogram Matched Image');
figure; imhist(B); title('mathed hist');