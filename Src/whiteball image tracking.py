import cv2

import numpy as np

frame = cv2.imread('ex4.jpeg')
# frame1 = cv2.imread('out.jpg')

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# define range of white color in HSV
# change it according to your need !
lower_white = np.array([0, 0, 168])
upper_white = np.array([172, 111, 255])

# Threshold the HSV image to get only white colors
mask = cv2.inRange(hsv, lower_white, upper_white)
# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame,frame, mask= mask)
median = cv2.medianBlur(res, 9)
gray = cv2.cvtColor(median,cv2.COLOR_BGR2GRAY)



print(np.count_nonzero(gray))
edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,200)
print(lines)
# print(lines)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)

# th2 = cv2.adaptiveThreshold(mask, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)

cv2.imshow('frame',frame)
# cv2.imshow('raspiimage',frame1)
cv2.imshow('Median',median)
# cv2.imshow('th2', th2)



cv2.waitKey(0)
cv2.destroyAllWindows()

'''
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# define range of white color in HSV
# change it according to your need !
lower_white = np.array([0, 0, 168])
upper_white = np.array([172, 111, 255])

# Threshold the HSV image to get only white colors
mask = cv2.inRange(hsv, lower_white, upper_white)
# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame,frame, mask= mask)
# median = cv2.medianBlur(res, 5)
blur = cv2.GaussianBlur(res,(5,5),0)
blur = cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
# roi = blur[600:900,600:1000]
ret,thresh1 = cv2.threshold(blur,100,255,cv2.THRESH_BINARY_INV)
print('ret:',ret)
# Erode to eliminate noise, Dilate to restore eroded parts of image
mask = cv2.erode(thresh1, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)


# Find all contours in frame
contours, hierarchy = cv2.findContours(mask.copy(),1,cv2.CHAIN_APPROX_NONE)
print(contours)
if len(contours) > 0:
		# Find largest contour area and image moments
		c = max(contours, key = cv2.contourArea)
		M = cv2.moments(c)

		# Find x-axis centroid using image moments
		cx = int(M['m10']/M['m00'])

		if cx >= 150:
			print('stop1')

		if ((cx < 150) and (cx > 40)):print('run')

		if cx <= 40:print('stop2')
cv2.imshow('mask',mask)
'''
