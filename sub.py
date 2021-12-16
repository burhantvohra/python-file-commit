import cv2
import numpy
from matplotlib import pyplot as plt
img1=cv2.imread('1111.jpeg')
img2=cv2.imread('1112.jpeg')
dst=cv2.addWeighted(img1,0.9,img2,0.2,0)
img3=img1-img2;
img4=cv2.subtract(img1,img2)
plt.figure(1);
plt.subplot(2,3,1),plt.imshow(img1),plt.title('image1')
plt.subplot(2,3,2),plt.imshow(img2),plt.title('image2')
plt.subplot(2,3,3),plt.imshow(dst),plt.title('weighted')
plt.subplot(2,3,4),plt.imshow(img3),plt.title('direct subtract')
plt.subplot(2,3,5),plt.imshow(img4),plt.title('overlap subtract')

#cv2.imshow("original",img1)
#cv2.waitkey(0)
#cv2.destroyallwindows()

#ret,bimg1=cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
#ret,bimg2=cv2.threshold(img2,127,255,cv2.THRESH_BINARY_INV)
#plt.subplot(2,3,4),plt.imshow(bimg1,'gray'),plt.title('binary img')
#plt.subplot(2,3,5),plt.imshow(bimg2,'gray'),plt.title('inv binary img')
plt.show()
