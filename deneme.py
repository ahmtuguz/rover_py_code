from typing import Counter
from xmlrpc.client import boolean
import cv2 
import os

from numpy import False_

j=3
sayac=1
for i in range(1,j):
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    while True:
        try:
            check, frame = webcam.read()
            print(check) #prints true as long as the webcam is running
            print(frame) #prints matrix values of each framecd 
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(310)
            path = "/home/uguz/Desktop/IP-Mineral" + str(sayac)
            os.mkdir(path)
            #os.makedirs(path, exist_ok = True)
            
            if key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
            
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
    