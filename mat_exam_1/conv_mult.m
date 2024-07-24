close all
clear all
Img = imread('cameraman.tif');
figure(1);imshow(Img);title('Original Image');
pause

ImgD=double(Img);
[M,N]=size(Img);
K=10;
sigma=2*K;
x=[1:(2*K+1)];
x=exp(-(x-K-1).^2./sigma);
kernel=x'*x;
kernel=kernel/(sum(sum(kernel)));
[K,K]=size(kernel);
imagesc(kernel)

pause
ImgP=zeros(M+K-1,N+K-1);
ImgP(1:M,1:N)=ImgD;
kerP=zeros(M+K-1,N+K-1);
kerP(1:K,1:K)=kernel;

figure(2);imagesc(kerP);title('kernel');
set(2,'position',[100 300 200 200])
figure(1);imshow(uint8(ImgP));title('Original Image');
set(1,'position',[500 300 200 200])

pause

kerF=fftshift(fft2(kerP));
ImgF=fftshift(fft2(ImgP));
figure(3)
imagesc(log10(abs(kerF)));
title('kernel');
figure(4)
imagesc(log10(abs(ImgF)));
title('Original Image');
set(3,'position',[100 10 200 200])
set(4,'position',[500 10 200 200])

pause
BlImgF=ImgF.*kerF;
BlImg=ifft2(fftshift(BlImgF));
figure(5)
imshow(uint8(real(BlImg)))
set(5,'position',[300 10 200 200])
pause

RBimgF=BlImgF./kerF;
RBimg=ifft2(fftshift(RBimgF));
figure(6)
imshow(uint8(real(RBimg)))
set(6,'position',[300 300 200 200])

pause
F7=(BlImgF+5e-4*rand(size(BlImgF)))./kerF;
I7=ifft2(fftshift(F7));
figure(6)
imshow(uint8(real(I7)))
set(6,'position',[300 300 200 200])

pause

F8=zeros(size(F7));
c=floor(0.5*size(F7));
cn=100;
F8(c(1)-cn:c(1)+cn,c(2)-cn:c(2)+cn)=ones(2*cn+1,2*cn+1);
figure(2)
imshow(F8)
set(2,'position',[100 300 200 200])

F7=F7.*F8;
I7=ifft2(fftshift(F7));
figure(6)
imshow(uint8(real(I7)))
set(6,'position',[300 300 200 200])
