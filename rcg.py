import cv2, sys, numpy, os
import numpy as np

import requests
import serial

import time
import argparse
import threading




import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

for port, desc, hwid in sorted(ports):
        #print("{}: {} [{}]".format(port, desc, hwid))
        print("{}: {}".format(port, desc))

#port = "/dev/ttyUSB0" # linux
# port = "COM5" # WINDOWS
# baud = 9600

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--port", required=False,
    help = "com port of arduino")

ap.add_argument("-l", "--location", required=False, default="Haridwar",
    help = "location of installation")

args = vars(ap.parse_args())


port = args['port']
date = args['location']



def notificationChallan():
    time.sleep(5)


notificationThread = threading.Thread(target=notificationChallan)

# serialPort = serial.Serial(port, baud, timeout=1)
# # open the serial port
# if serialPort.isOpen():
#     print(serialPort.name + ' is open...')



host = 'http://localhost:8080/ToolGateTheft/'

LOCATION="Haridwar"


def checkWithServerChallan(vehicle):
    final_url  = host + 'get-challan-status.jsp'    
    request_data = {'get_status':"temp",
                         'vehicle':vehicle,
                         'location':LOCATION
                         }
    print(request_data)
    reuquest_result = requests.post(final_url, request_data)
    print(reuquest_result.text)
    return reuquest_result
    

def checkWithServer(vehicle):
    final_url  = host + 'get-toll-status.jsp'    
    request_data = {'get_status':"temp",
                         'vehicle':vehicle,
                         'location':LOCATION
                         }
    print(request_data)
    reuquest_result = requests.post(final_url, request_data)
    print(reuquest_result.text)
    return reuquest_result
    
    
    
def processGate(serialPort):
    print("Command opening sent arduino") #replace with arduiono communication
    serialPort.write('OPEN_BARIOR\r\n'.encode('ascii'))
    oprationStatus = serialPort.read_until('\r'.encode('ascii'));
    print(oprationStatus)
    oprationStatus = serialPort.readline();
    time.sleep(5)
    oprationStatus = serialPort.readline();
    serialPort.write('CLOSE_BARIOR\r\n'.encode('ascii'))
    oprationStatus = serialPort.read_until('\r'.encode('ascii'));
    print(oprationStatus)
    oprationStatus = serialPort.readline();
    


import re
def getValidateNumber(text):
    rs = re.search(".{2}\d{2}.{2}\d{4}", text)
    if rs is None:
        return None
    vehicleNumber =  rs.group()
    return vehicleNumber



from PIL import Image
import pytesseract







pytesseract.pytesseract.tesseract_cmd = 'C:\Tesseract-OCR\\tesseract'
tessdata_dir_config = '--tessdata-dir "C:\Tesseract-OCR\\tessdata"'



cascade_fn =  'cascade.xml'
cascade = cv2.CascadeClassifier(cascade_fn)

(im_width, im_height) = (320, 240)


def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)




webcam = cv2.VideoCapture(0)

confirmation_count  = 0

response = ""
textStr =""

# Load an color image in color
challan_notification = cv2.imread('Picture1.png',cv2.IMREAD_COLOR)
theft_notification = cv2.imread('theft.png',cv2.IMREAD_COLOR)
allow_notification = cv2.imread('allowed.png',cv2.IMREAD_COLOR)
toll_not_notification = cv2.imread('toll_not_p.png',cv2.IMREAD_COLOR)
#cv2.imshow('Notification', challan_notification) 

loop_count = 0
notfied = False

while True:

    
    # Loop until the camera is working
    rval = False
    while(not rval):
        # Put the image from the webcam into 'frame'
        (rval, frame) = webcam.read()
        if(not rval):
            print("Failed to open webcam. Trying again...")
    
   
    
    loop_count +=1
    
    if loop_count < 0: # for some delay
        continue
    
    if loop_count > 60 and notfied == True:
        notfied = False
        cv2.destroyWindow('Notification')
    
    
    # Get image size
    height, width, channels = frame.shape
    
    #resize image to speed up process
    resized_frame = cv2.resize(frame, (im_width, im_height))
   
    #detect using haarcascade
    rects = detect(resized_frame, cascade)
   
   
    resized_frame_copy = resized_frame.copy()
    #draw react on identyfied object
    draw_rects(resized_frame_copy, rects, (0, 255, 0))
    
    
    textStr = ""
    response = ""
    
    
    if(len(rects) > 0):
        x1, y1, x2, y2 = rects[0]
        cv2.putText(resized_frame_copy, 'Numebr Plate', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        #print("Yes")#for debug
        xd = (x2-x1)
        yd = (y2-y1)#for debug
        #print("X:% Y:%i",xd,yd)
        if xd > 220 and yd >70:
            confirmation_count+=1
        else:
            confirmation_count = 0
            print("Size is small")
        
    else:
        
        confirmation_count = 0
        
        
    cv2.imshow('Number-Plate', resized_frame_copy)

    reg_number = None
    if confirmation_count > 20:
        print("Number plate is confirmed detected")
        confirmation_count = 21
        
       
        
        if(len(rects) > 0):
            x1, y1, x2, y2 = rects[0]
            crop_img = resized_frame[y1:y2, x1:x2]
            cv2.imshow('Croped-Number-Plate', crop_img)

            img_p = cv2.cvtColor(crop_img, cv2.COLOR_BGR2RGB)
            im_pil = Image.fromarray(img_p)
            textStr = pytesseract.image_to_string( im_pil, lang='eng', config=tessdata_dir_config)
            textStr = textStr.replace(" ", "")
            print(textStr)
            reg_number = getValidateNumber(textStr)
            print("Refine:",reg_number)
                
            confirmation_count = 0

    
    key = cv2.waitKey(1) & 0xFF
    
   
    if reg_number is not None:
    
        # challanResponse = checkWithServerChallan(reg_number)
        # challan_status = challanResponse.text
        # finalStr = str(challan_status.encode('utf-8'))
        # # THEFT_VEHICLE_DETECTED\n
        # # THE_VEHICLE_NOT_PAID\n
        # if finalStr.__contains__("THEFT_VEHICLE_DETECTED"):
        #     print("Theft detected")
        #     cv2.imshow('Notification', theft_notification)
        #     loop_count = 0
        #     notfied = True
        #     continue
        # elif finalStr.__contains__("THE_VEHICLE_NOT_PAID"):
        #     print("Vehicle is not Paid")
        #     cv2.imshow('Notification', toll_not_notification)
        #     loop_count = 0
        #     notfied = True
        #     continue
        # else:
        #     print("Vehicle is not Paid")
        #     cv2.imshow('Notification', toll_not_notification)
        #     loop_count = 0
        #     notfied = True
            
             
        
        response = checkWithServer(reg_number)
        action = response.text
        print("Response")
        finalStr = str(action.encode('utf-8'))
        print( finalStr )
        
        if finalStr.__contains__("THEFT_VEHICLE_DETECTED"):
            print("Theft detected")
            cv2.imshow('Notification', theft_notification)
            loop_count = 0
            notfied = True
            continue
        elif finalStr.__contains__("THE_VEHICLE_NOT_PAID"):
            print("Vehicle is not Paid")
            cv2.imshow('Notification', toll_not_notification)
            loop_count = 0
            notfied = True
            continue            
        else:
             print("Vehicle is allowed paid.")
             loop_count = -60
             notfied = True
             cv2.imshow('Notification', allow_notification)
             
        cv2.destroyWindow('Croped-Number-Plate')
        
        
    if key == ord("q"):
        break
        
        
        
        
        
        
        
        
        
        
        
        
        