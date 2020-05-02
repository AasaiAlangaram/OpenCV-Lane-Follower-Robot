import cv2
import numpy as np
import math
import serial
import picamera
import picamera.array

theta=0
minLineLength = 5
maxLineGap = 10

ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)           # linux

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = picamera.array.PiRGBArray(camera, size = (640, 480))
time.sleep (0.1)
for frame in camera.capture_continuous (rawCapture, format = "bgr", use_video_port = True):
    image = frame.array
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
        ser.write(chr(4).encode())
        print("left")
    if(theta<-threshold):
        ser.write(chr(3).encode())
        print("right")
    if(abs(theta)<threshold):
        ser.write(chr(1).encode())
        print("straight")

    theta=0

    cv2.imshow("Frame",image)
    # Press Q on keyboard to  exit
    if cv2.waitKey(1) == ord('q'):
        print('Streaming Stopped because of key pressed event')
        break

# Closes all the frames
cv2.destroyAllWindows()