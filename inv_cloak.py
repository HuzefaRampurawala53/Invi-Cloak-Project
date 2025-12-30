import cv2 as cv
import time
import numpy as np
print("Capturing the background Please get away from the camera")
print("It will roughly take 5 seconds...")
cap=cv.VideoCapture(0)

time.sleep(3)
background = 0
for i in range(30):
    ret, background = cap.read()

background=cv.flip(background,1)  #Mostly the picture captured from default webcam is not proper so we need to flip it :)
print("Backgroud captured\nNow you can come infront of the camera")
while cap.isOpened():   
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv.flip(frame,1)

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lower_blue = np.array([94, 80, 2]) #min Hue , Sat , Brightness
    upper_blue = np.array([126, 255, 255])  #max Hue , Sat , Brightness


    mask=cv.inRange(hsv, lower_blue, upper_blue)
    area = cv.countNonZero(mask)
    if area < 3000:
        kernel =  np.ones((7,7), np.uint8)
    else:
        kernel =  np.ones((5, 5), np.uint8)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN,kernel, iterations=1)
    mask = cv.dilate(mask,  kernel,iterations=1)
    mask_inv = cv.bitwise_not(mask)
    #background = cv.GaussianBlur(background,(7,7),0)

    res1 = cv.bitwise_and(background,background,mask=mask) #The background where there is cloak
    res2 = cv.bitwise_and(frame,frame,mask=mask_inv) #The frame where there is no cloak
    final = cv.addWeighted(res1, 1, res2, 1, 0)

    # final = cv.bitwise_or(res1, res2)  We can use any of the lines add or 'or'
    #cv.add(res1,res2)
    cv.imshow('Invisible',final)
    #cv.imshow("Mask", mask)
    #cv.imshow('Mask inverse',mask_inv)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
print("Hope you liked it!!! :)")
print("ThankYou")