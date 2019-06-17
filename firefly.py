import numpy as np
import cv2

def main():
    #16.176 frames in the video
    cap = cv2.VideoCapture("cap.wmv")
    #Initialisation of frame_counting variable
    frame_count=0;
    #Loop as long as there's a frame to analyze
    while cap.grab():
        #Initialisation of supporting variables
        flag, frame = cap.retrieve()
        #Adding current frame to frame counter
        frame_count+=1
        print((frame_count))
        imCrop = frame[80:95,150:175]
        finder(imCrop)
        #Escape
        if cv2.waitKey(10) == 27:
            break

def finder(im):
    # Set up the detector with necessary parameters
    params = cv2.SimpleBlobDetector_Params()
    params.filterByColor = 1
    params.blobColor=255
    detector = cv2.SimpleBlobDetector_create(params)
    # Detect blobs
    keypoints = detector.detect(im)
    #Drawing red cicles around said blobs
    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("Keypoints", im_with_keypoints)

main()
