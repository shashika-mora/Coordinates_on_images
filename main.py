from typing import *
import cv2
import numpy as np




def click_event(event: int, x: int, y: int, flags: int, param: Any) -> None:
    font = cv2.FONT_HERSHEY_SIMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        cv2.putText(image, str(x) + ", " + str(y), (x, y), font, 1, (255, 255, 255), 2)
        cv2.imshow('Image', image)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x, y)
        b,g,r = image[y,x]
        cv2.putText(image, str(b) + ", " + str(g) + ", " + str(r), (x, y), font, 1, (int(b), int(g), int(r)), 2)
        cv2.imshow('Image', image)

    
if __name__ == '__main__':
    # Read the image and display it
    image = cv2.imread('image.png')
    cv2.imshow('Image', image)

    # Set the mouse callback function
    cv2.setMouseCallback('Image', click_event)

    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()