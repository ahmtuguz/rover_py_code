from typing import Counter
from xmlrpc.client import boolean
import cv2 
import os

from numpy import False_

j=3
sayac=1

path = "/home/uguz/Desktop/IP-Mineral" + str(sayac)+ "/"
boolean_x=os.path.exists(os.path.join(os.getcwd(),path ))
if(boolean_x==True):
    path = "/home/uguz/Desktop/IP-Mineral" + str(sayac+1)+ "/"
os.mkdir(path)
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
            
            # boolean_x=os.path.exists(os.path.join(os.getcwd(),path ))
            # if(boolean_x==False):
            #     path = "/home/uguz/Desktop/IP-Mineral" + str(sayac+1)+ ""
            #path = '/home/yildizrover/Desktop/IP-Mineral/'
            #os.mkdir("/home/yildizrover/Desktop/IP-Mineral/")

            #os.makedirs(path, exist_ok = True)
            if key == ord('s'): 
                cv2.imwrite(str(path) + 'saved_img.jpg',img=frame)
                #cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()
                #img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                #img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                print("Processing image...")
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                file_name = str(path)+"img" + str(i) + ".jpg"
                #os.rename(path+'/home/yildizrover/Desktop/IP-Mineral/saved_img.jpg',file_name)
                os.rename(str(path)+'saved_img.jpg',file_name)
                #print("Converting RGB image to grayscale...")
                #gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                #print("Converted RGB image to grayscale...")
                #print("Resizing image to 28x28 scale...")
                #img_ = cv2.resize(gray,(28,28))
                #print("Resized...")
                #img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                print("Image saved!")
                
                # if(i==j):
                #     path="/home/uguz/Desktop/IP-Mineral" + str(sayac+1)+ "/"   
                #     sayac+=1

                #cv2.waitKey(5000)
                
                break
            elif key == ord('q'):
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
    