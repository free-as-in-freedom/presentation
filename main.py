"""
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""

import cv2 
import pyautogui
import numpy as np
import threading
import queue
import os

def show_webcam(mirror=False):
    #user input queue
    q = queue.Queue()
    user_input = None
    thread = None

    #set video capture
    cap = cv2.VideoCapture(0)

    #video codec and recording setup
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    #camera loop
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            #flip camera perspective
            if mirror:
                frame = cv2.flip(frame,1)
                
            # output the frame to be saved
            out.write(frame)

            #display frame
            cv2.imshow('Frame',frame)
            
            #USER INPUT LOOP
            #get user input
            key = cv2.waitKey(25) & 0xFF

            #quit program
            if key == ord('q'):
                break
            
            #get filename from user
            elif key == ord("w") and thread == None:
                thread = threading.Thread(target=get_filename, args=(q,))
                thread.start()
            
            #commit filename and show image file
            elif key == ord("c") and thread != None:
                thread.join()
                filename = q.get()
                #print(filename)
                process_image(filename, frame)
                thread = None
            
        else: 
            break

    out.release()
    cap.release()

    cv2.destroyAllWindows()

def process_image(filename, frame):
    file_path = f"images/{filename}"
    
    #check if file path exists
    if not os.path.exists(file_path):
        print(f"\"{file_path}\" is not a valid file path. Try agian by pressing \"w\"\n")
        return
    
    image = cv2.imread("file_path")
    
    #process image
    frame_height, frame_width, frame_channels = frame.cv2.get_size()
    image_size = (frame_height//5, frame_width//5)

    correct_size_image = cv2.resize(image, image(size[0], image_size[1]))
    return correct_size_image



        
        

def get_filename(q):
    user_input = input("Input an image filename here: ")
    q.put(user_input)


def show_screen():
	image = pyautogui.screenshot()
	image = cv2.cvtColor(np.array(image),
				 cv2.COLOR_RGB2BGR)
	cv2.imshow("",image) 

def main():
    directory = "images"
    if not os.path.exists(directory):
        os.makedirs(directory)
    show_webcam(mirror=True)
	#show_screen()

if __name__ == '__main__':
    main()
