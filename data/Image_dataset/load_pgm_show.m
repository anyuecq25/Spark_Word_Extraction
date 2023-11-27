img1=imread('M002068_27_135_45.pgm');
img2=imread('M005442_15_45_135.pgm');
img3=imread('M008242_33_180_0.pgm');
img4=imread('M007376_11_45_45.pgm');
img5=imread('M001134_12_45_67.5.pgm');

img11=imread('M002068_27_135_45_hog.pgm');
img22=imread('M005442_15_45_135_hog.pgm');
img33=imread('M008242_33_180_0_hog.pgm');
img44=imread('M007376_11_45_45_hog.pgm');
img55=imread('M001134_12_45_67.5_hog.pgm');
thresh1 = graythresh(img11); % 针对原图自动确定二值化阈值，阈值越大图像越黑，越小越白
img11 = imbinarize(img11,thresh1); % 对图像直接进行二值化
thresh1 = graythresh(img22); % 针对原图自动确定二值化阈值，阈值越大图像越黑，越小越白
img22 = imbinarize(img22,thresh1); % 对图像直接进行二值化
thresh1 = graythresh(img33); % 针对原图自动确定二值化阈值，阈值越大图像越黑，越小越白
img33 = imbinarize(img33,thresh1); % 对图像直接进行二值化
thresh1 = graythresh(img44); % 针对原图自动确定二值化阈值，阈值越大图像越黑，越小越白
img44 = imbinarize(img44,thresh1); % 对图像直接进行二值化
thresh1 = graythresh(img55); % 针对原图自动确定二值化阈值，阈值越大图像越黑，越小越白
img55 = imbinarize(img55,thresh1); % 对图像直接进行二值化
%title('M002068')

images = {img1, img2, img3, img4,img5, img11, img22, img33, img44,img55};
%set(gca, 'LooseInset', [0,0,0,0]);
figure; montage(images,'Size',[2 5],'BorderSize',15,'BackgroundColor','white');
% text(120,0.5,'M002068','FontSize',12)
% text(420,0.5,'M005442')
% text(730,0.5,'M008242')
% text(1050,0.5,'M007376')
% text(1350,0.5,'M001134')

%title('Illustration of Hog Features');