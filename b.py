#!/usr/bin/env python

# import the necessary packages
from imutils.video import VideoStream
import argparse
import imutils
import time
import cv2
import sys

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--type", type=str,
   default="DICT_4X4_50",
   help="type of ArUCo tag to detect")
args = vars(ap.parse_args())

# define names of each possible ArUco tag OpenCV supports
ARUCO_DICT = {
   "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
   "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
   "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
   "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
   "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
   "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
   "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
   "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
   "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
   "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
   "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
   "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
   "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
   "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
   "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
   "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
   "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
#	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
#	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
#	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
#	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}

# verify that the supplied ArUCo tag exists and is supported by
# OpenCV
if ARUCO_DICT.get(args["type"], None) is None:
   print("[INFO] ArUCo tag of '{}' is not supported".format(
      args["type"]))
   sys.exit(0)

# load the ArUCo dictionary and grab the ArUCo parameters
print("[INFO] detecting '{}' tags...".format(args["type"]))
arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])
arucoParams = cv2.aruco.DetectorParameters_create()

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=2).start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:
   # grab the frame from the threaded video stream and resize it
   # to have a maximum width of 600 pixels
   frame = vs.read()
   frame = imutils.resize(frame, width=1000)

   # detect ArUco markers in the input frame
   (corners, ids, rejected) = cv2.aruco.detectMarkers(frame,
      arucoDict, parameters=arucoParams)

   # verify *at least* one ArUco marker was detected
   if len(corners) > 0:
      # flatten the ArUco IDs list
      ids = ids.flatten()
      markers_x=[]
      markers_y=[]
      #print(ids)
      new_id_value=[]
      old_id_value=[]
      orta_nokta=[]
      i=0
      # loop over the detected ArUCo corners
      for (markerCorner, markerID) in zip(corners, ids):
         # extract the marker corners (which are always returned
         # in top-left, top-right, bottom-right, and bottom-left
         # order)
         corners = markerCorner.reshape((4, 2))
         (topLeft, topRight, bottomRight, bottomLeft) = corners
         i+=1
         print(i)
         # convert each of the (x, y)-coordinate pairs to integers
         topRight = (int(topRight[0]), int(topRight[1]))
         bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
         bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
         topLeft = (int(topLeft[0]), int(topLeft[1]))

         # draw the bounding box of the ArUCo detection
         cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
         cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
         cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
         cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)

         # compute and draw the center (x, y)-coordinates of the
         # ArUco marker
         cX = int((topLeft[0] + bottomRight[0]) / 2.0)
         #time.sleep(5)
         cY = int((topLeft[1] + bottomRight[1]) / 2.0)
         print("CX:",cX,"CY:",cY)
         if i%2==1:
            old_id_value=[cX,cY]
            #print("old: ",old_id_value)
            # if len(ids)>1:
            #    orta_nokta=[int((new_id_value[0] - old_id_value[0])),int((new_id_value[1] - old_id_value[1]))]
            #    print(orta_nokta)
         elif i>0 and i%2==0:
            new_id_value=[cX,cY]
            #print("new: ",new_id_value[0])
            # if len(ids)>1:
            #    orta_nokta=[int((new_id_value[0] - old_id_value[0])),int((new_id_value[1] - old_id_value[1]))]
            #    print(orta_nokta)
         
         # if len(ids)==2:
         #    print(old_id_value[0])
         #    print(new_id_value[0])

         
         
         #markers_x.append(cX)
         #markers_y.append(cY)
         # print("1. "+str(cX[0])+ "2. "+ str(cX[1]))
         # print("1. "+str(cY[0])+ "2. "+ str(cY[1]))
      
         cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)
            
         # draw the ArUco marker ID on the frame
         cv2.putText(frame, str(markerID),
            (topLeft[0], topLeft[1] - 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 255, 0), 2)
            
   # show the output frame
   cv2.imshow("Frame", frame)
   key = cv2.waitKey(1) & 0xFF

   # if the `q` key was pressed, break from the loop
   if key == ord("q"):
      break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()