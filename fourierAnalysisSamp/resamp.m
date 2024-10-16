close all;
clear all;
A=imread('cameraman.jpg');
figure(1);   imshow(A); set(1,'position',[836   510   420   342]);
B=interp2(A(1:5:end,1:5:end),5,'nearest');
figure(2) ; imshow(B); set(2,'position',[ 833    73   420   342]);
title('down sample');
H = fspecial('average',10);
C=filter2(H,A);
D=interp2(C(1:5:end,1:5:end),5,'nearest');
figure(3);  imshow(uint8(D)); set(3,'position',[ 364    74   420   342]);
title('prefilterd');