
from fileinput import filename
from typing import Counter
from xmlrpc.client import boolean
import cv2
import os

from numpy import False_
class Science():
    def __init__(self):
        self.PATH_TO_DIRECS = "/home/alperenlcr/python_debug_c_p/"
        self.dynamic_path = self.PATH_TO_DIRECS
        self.img_count = 1
        self.mineral_count = 1
        self.toprak_count = 1


    def image_saver(self):

        # program to capture single image from webcam in python

        # importing OpenCV library

        # initialize the camera
        # If you have multiple camera connected with
        # current device, assign a value in cam_port
        # variable according to that
        cam_port = 0
        cam = cv2.VideoCapture(cam_port)

        # reading the input using the camera
        result, image = cam.read()

        # If image will detected without any error,
        # show result
        if result:
            file_name = str(self.dynamic_path)+"img" + str(self.img_count) + ".jpg"

            # showing result, it take frame name and image
            # output
            # saving image in local storage
            cv2.imwrite(file_name, image)

            # If keyboard interrupt occurs, destroy image
            # window
            cv2.waitKey(0)

        # If captured image is corrupted, moving to else part
        else:
            print("No image detected. Please! try again")
        cam.release()

    def image_saver2(self):
        path = self.dynamic_path
        #print(path) #gets it correctly
        file_name = str(path)+"img" + str(self.img_count) + ".jpg"
        #print(file_name)
        #cv2.imwrite(str(path) + file_name, img=self.frame)  # O O O O why path + f_n
        cv2.imwrite(file_name, img=self.frame)
        print("Image saved!")
        self.img_count += 1


    def create_mineral_folder(self, ref="IP-Mineral"):
        self.img_count = 1
        sayac = self.mineral_count
        self.mineral_count += 1
        while True:
            path = self.PATH_TO_DIRECS + ref + str(sayac)+ "/"
            boolean_x=os.path.exists(os.path.join(os.getcwd(),path ))
            if(boolean_x==True):
                path = self.PATH_TO_DIRECS + str(sayac+1)+ "/"
            else:
                break
        self.dynamic_path = path
        os.mkdir(path)

    def display(self):
        try:
            webcam = cv2.VideoCapture(0)
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
            #    cv2.imwrite(str(path) + 'saved_img.jpg',img=frame)
                #cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()
                #img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                #img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                print("Processing image...")
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            #    file_name = str(path)+"img" + str(i) + ".jpg"
                #os.rename(path+'/home/yildizrover/Desktop/IP-Mineral/saved_img.jpg',file_name)
            #    os.rename(str(path)+'saved_img.jpg',file_name)
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

            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
            
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()

S = Science()
# j=3

# for i in range(1,j):
#     key = cv2. waitKey(1)
#     webcam = cv2.VideoCapture(0)
#     while True:
#         try:
#             check, frame = webcam.read()
#             print(check) #prints true as long as the webcam is running
#             print(frame) #prints matrix values of each framecd 
#             cv2.imshow("Capturing", frame)
#             key = cv2.waitKey(310)
            
#             # boolean_x=os.path.exists(os.path.join(os.getcwd(),path ))
#             # if(boolean_x==False):
#             #     path = "/home/uguz/Desktop/IP-Mineral" + str(sayac+1)+ ""
#             #path = '/home/yildizrover/Desktop/IP-Mineral/'
#             #os.mkdir("/home/yildizrover/Desktop/IP-Mineral/")

#             #os.makedirs(path, exist_ok = True)
#             if key == ord('s'): 
#                 cv2.imwrite(str(path) + 'saved_img.jpg',img=frame)
#                 #cv2.imwrite(filename='saved_img.jpg', img=frame)
#                 webcam.release()
#                 #img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
#                 #img_new = cv2.imshow("Captured Image", img_new)
#                 cv2.waitKey(1650)
#                 cv2.destroyAllWindows()
#                 print("Processing image...")
#                 img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
#                 file_name = str(path)+"img" + str(i) + ".jpg"
#                 #os.rename(path+'/home/yildizrover/Desktop/IP-Mineral/saved_img.jpg',file_name)
#                 os.rename(str(path)+'saved_img.jpg',file_name)
#                 #print("Converting RGB image to grayscale...")
#                 #gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
#                 #print("Converted RGB image to grayscale...")
#                 #print("Resizing image to 28x28 scale...")
#                 #img_ = cv2.resize(gray,(28,28))
#                 #print("Resized...")
#                 #img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
#                 print("Image saved!")
                
#                 # if(i==j):
#                 #     path="/home/uguz/Desktop/IP-Mineral" + str(sayac+1)+ "/"   
#                 #     sayac+=1

#                 #cv2.waitKey(5000)
                
#                 break
#             elif key == ord('q'):
#                 print("Turning off camera.")
#                 webcam.release()
#                 print("Camera off.")
#                 print("Program ended.")
#                 cv2.destroyAllWindows()
#                 break
            
#         except(KeyboardInterrupt):
#             print("Turning off camera.")
#             webcam.release()
#             print("Camera off.")
#             print("Program ended.")
#             cv2.destroyAllWindows()
#             break