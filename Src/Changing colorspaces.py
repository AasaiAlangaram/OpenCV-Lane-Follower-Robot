import cv2

import numpy as np
'''
flags = [i for i in dir(cv) if i.startswith('COLOR_')]

print('No of Color-space conversion method in opencv:',len(flags))
'''

# import cv2
# import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of white color in HSV
    # change it according to your need !
    lower_white = np.array([0, 0, 168])
    upper_white = np.array([172, 111, 255])

    # Threshold the HSV image to get only white colors
    mask = cv2.inRange(hsv, lower_white, upper_white)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    median = cv2.medianBlur(res, 5)
    roi = median[200:400, 150:400]
    cv2.imshow("ROI", roi)
    th2 = cv2.adaptiveThreshold(mask, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)


    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',median)
    cv2.imshow('th2', th2)

    # Press Q on keyboard to  exit
    if cv2.waitKey(1) == ord('q'):
        print('Streaming Stopped because of key pressed event')
        break

cv2.destroyAllWindows()