import numpy as np
import cv2

vid=cv2.VideoCapture('cap.wmv')
ret, frame = vid.read()
while(ret):
    ret, frame = vid.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale, (11, 11), 0)
    # showing bright regions of blurred photo
    brightest = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)[1]
    # perform a series of erosions and dilations to remove
    # any small blobs of noise from the thresholded image
    brightest = cv2.erode(brightest, None, iterations=2)
    brightest = cv2.dilate(brightest, None, iterations=4)
    cv2.imshow('frame',brightest)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
