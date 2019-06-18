# Federico Tondolo
# Summer 2019 at the Columbia University Medical Center 
import numpy as np
import ffmpy
import cv2
import os

def main():
    # Creating OUTPUT directory
    os.mkdir('OUTPUT')
    # Loops for every file inside current dir
    for filename in os.listdir('.'):
        # If file is a video file
        if (filename.endswith(".wmv")):
            cap = cv2.VideoCapture(filename)
            # Initialisation of frame_counting variable
            frame_count=0
            # Initialisation of lightbulb activations count
            count=0
            # Initialisation of variable defining the next valid frame
            next_valid=0
            # Loop as long as there's a frame to analyze
            while cap.grab():
                # Adding current frame to frame counter
                frame_count+=1
                # If frame is bit within 21 seconds of first trigger
                if (frame_count>=next_valid):
                    # Initialisation of supporting variables
                    flag, frame = cap.retrieve()
                    # Cropping and Brightening
                    imCrop = frame[80:95,150:175]
                    brightest = cv2.threshold(imCrop, 200, 255, cv2.THRESH_BINARY)[1]
                    if finder(brightest):
                        count+=1
                        start= (frame_count/30)-20
                        next_valid=((start+60)*30)
                        os.system('ffmpeg -i {0} -ss {1} -t 40 ./OUTPUT/output_{2}-{3}.wmv'.format(filename, start, filename[:-4], count))
         # If file is not a video 
        else:
            continue
        
def finder(im):
    # Set up the detector with necessary parameters
    params = cv2.SimpleBlobDetector_Params()
    params.filterByColor = 1
    params.blobColor=255
    detector = cv2.SimpleBlobDetector_create(params)
    # Detect blobs
    keypoints = detector.detect(im)
    # Blob detected
    if len(keypoints):
        return 1
    
main()
