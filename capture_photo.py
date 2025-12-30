import cv2 as cv
import os
cap=cv.VideoCapture(0)
img_count = 0
img_path =  r'C:\Users\ADMIN\Documents\GitHub\Invi-Cloak-Project\Photos'
while True:
    ret,frame = cap.read()
    if not ret:
        break
    cv.flip(frame,1)
    cv.imshow('Video',frame)
    key = cv.waitKey(1) & 0xFF

    if key == ord('s'):
        img_count = img_count + 1
        filename = os.path.join(img_path,f"Photo_{img_count}.jpg")
        cv.imwrite(filename,frame)
        print("Image saved")
    elif key == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv.destroyAllWindows()

