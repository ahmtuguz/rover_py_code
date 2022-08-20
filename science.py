from pickle import TRUE
import rospy
from science_utils import *
from sensor_msgs.msg import Joy
import cv2

# PATH_TO_DIRECS ayarla utils'de

def button10():          # fotograf cek
    print("10")
    S.image_saver()

def button11():          # toprak icin klasor olustur
    print("11")
    S.create_mineral_folder()

def button12():          # tas icin klasor olustur
    print("12")


button_func_dict = {"10" : button10,
                    "11" : button11,
                    "12" : button12}

def callback(data):

    for button in data.buttons:
        if button == 1:
            msg = data.buttons.index(button)
            if msg == 10 or msg == 11 or msg == 9:
                button_func_dict[str(msg+1)]()

    for axe in data.axes:
        if axe != 0:
            msg = data.axes.index(axe)

    
    # while True:  #displaying the captured image
    #     cv2.imshow("im1",S.frame)
    #     if cv2.waitKey(1) & 0xFF == ord("y"):
    #         break


def joy_listener():
    
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("/joy", Joy, callback)
    #S.display()
    rospy.spin()

if __name__ == "__main__":
    joy_listener()