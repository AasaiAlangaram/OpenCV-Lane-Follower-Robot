
import cv2
import numpy as np
import math
import serial
# import picamera
# import picamera.array

theta=0
minLineLength = 5
maxLineGap = 10

# ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)           # linux


image = cv2.imread(r'C:\Users\aasai\Desktop\out.jpg')
image = cv2.resize(image,(500,300))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 85, 85)
lines = cv2.HoughLinesP(edged,1,np.pi/180,10,minLineLength,maxLineGap)
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
        theta=theta+math.atan2((y2-y1),(x2-x1))
        print(theta)
threshold=6
if(theta>threshold):

       print("left")
if(theta<-threshold):

    print("right")
if(abs(theta)<threshold):

    print("straight")
theta=0
cv2.imshow("Frame",image)
cv2.waitKey(0)
cv2.destroyAllWindows()