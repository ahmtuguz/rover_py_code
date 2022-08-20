import cv2  # importing cv
import imutils
import os
import os.path
 
# read an image as input using OpenCV
f = r'/home/uguz/Downloads/image_augmentation/images'
destination_path="/home/Downloads"
for file in os.listdir(f):
    f_img=f+"/"+file
    image = cv2.imread(f_img)
    Rotated_image = imutils.rotate(image, angle=270)
    cv2.imwrite(f_img,Rotated_image)