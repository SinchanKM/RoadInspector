import cv2
import numpy as np
import pygame
import time
#import smtplib
from matplotlib import pyplot as plt

def main():
 im = cv2.imread('indes__1_.jpg')
 img=im.copy()
 img11=im.copy()
# CODE TO CONVERT TO GRAYSCALE

#CONTOUR DETECTION CODE
 imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

 plt.subplot(331),plt.imshow(imgray),plt.title('GRAY')
 ret,thresh = cv2.threshold(imgray,208,255,cv2.THRESH_BINARY)
 kernel = np.ones((3,3),np.uint8)
 thresh = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
 cv2.imshow("Thresh",thresh)
 image1, contours1, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# image2, contours2, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.imshow("Image2",image2)

 img1 = image1.copy()
# img2 = image2.copy()

 out = cv2.drawContours(im, contours1, -1, (0,0,255), 2)
# out = cv2.drawContours(im, contours2, -1, (250,0,0),1)
# out = np.hstack([img1, img2])


 cv2.waitKey(0)
 plt.xticks([]), plt.yticks([])
 cnt = max(contours1, key=cv2.contourArea)
 # cnt = contours1[0]
 print(cnt)
 M = cv2.moments(cnt)
 print(M)
 perimeter = cv2.arcLength(cnt,True)
 print (perimeter)
 area = cv2.contourArea(cnt)
 print (area)
 epsilon = 0.01*cv2.arcLength(cnt,True)
 approx = cv2.approxPolyDP(cnt,epsilon,True)
 print (epsilon)
 print (approx)
 cv2.drawContours(img, cnt, -1, (0, 255, 0), 3)
 cv2.drawContours(img, [approx], -1, (0, 0, 255), 3)
 # cv2.imshow("Approx",img)
 # cv2.imshow("out",out)
 x,y,w,h = cv2.boundingRect(cnt)
 cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
 cv2.imshow("Rectangle",img )
 # cv2.imshow("Show",im)
 cv2.waitKey()
 cv2.destroyAllWindows()
 hull = cv2.convexHull(cnt)
 k = cv2.isContourConvex(approx)

#to check convexity
 print(k)
#blur
 blur = cv2.blur(img11,(5,5))
#guassian blur 
 gblur = cv2.GaussianBlur(img11,(5,5),0)
#median 
 median = cv2.medianBlur(img11,5)
#erosion
 kernel = np.ones((5,5),np.uint8)
 erosion = cv2.erode(median,kernel,iterations = 1)
 dilation = cv2.dilate(erosion,kernel,iterations = 5)
#erosion followed dilation
 closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
#canny edge detection
 edges = cv2.Canny(dilation,9,220)
#plotting using matplotlib
 plt.subplot(332),plt.imshow(blur),plt.title('BLURRED')
 plt.xticks([]), plt.yticks([])
 plt.subplot(333),plt.imshow(gblur),plt.title('guassianblur')
 plt.xticks([]), plt.yticks([])
 plt.subplot(334),plt.imshow(median),plt.title('Medianblur')
 plt.xticks([]), plt.yticks([])
 plt.subplot(337),plt.imshow(imgray,cmap = 'gray')
 plt.title('dilated Image'), plt.xticks([]), plt.yticks([])
 plt.subplot(338),plt.imshow(edges,cmap = 'gray')
 plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
 plt.subplot(335),plt.imshow(erosion),plt.title('EROSION')
 plt.xticks([]), plt.yticks([])
 plt.subplot(336),plt.imshow(closing),plt.title('closing')
 plt.xticks([]), plt.yticks([])
 # plt.show()
#alerting the driver


#content ="detection of pothole in locality basapura road hosur road junction "
#mail = smtplib.SMTP('smtp.gmail.com',587)
#mail.ehlo()
#mail.starttls()
#mail.login('harika3196@gmail.com','hariammu3196@gmail.com')
#mail.sendmail('fromemail','receiver',content)
#mail.close()
