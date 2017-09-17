############################################
## Import OpenCV
import numpy as np
import cv2
# Initialize camera
cap = cv2.VideoCapture(0)
############################################
cv2.waitKey(5)
############################################
## Video Loop
while(1):
    
    ## Read the image
    ret, frame = cap.read()
    height, width, channels = frame.shape 
    ## Do the processing
    res = cv2.resize(frame, (width/4,height/4), interpolation=cv2.INTER_CUBIC)
    ## Show the image
    cv2.imshow('image',res)
    
    key = cv2.waitKey(1)
    if (key & 0xFF) == ord("c"):
        cv2.imwrite("cap_image.jpg", frame)
        cv2.imshow("capture", frame)

    ## End the video loop
    if (key & 0xFF) == 27:  ## 27 - ASCII for escape key
        break
############################################

############################################
## Close and exit
cap.release()
cv2.destroyAllWindows()
############################################
