############################################
## Import OpenCV
import numpy
import cv2
############################################

############################################
## Read the image
img= cv2.imread('lion.jpg')
############################################

############################################
## Do the processing
############################################

############################################
## Show the image
cv2.imshow('image',img)
############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################
