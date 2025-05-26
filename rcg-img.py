import cv2, sys, numpy, os
import numpy as np

import requests
import serial

import time


from PIL import Image
import pytesseract



import re
def getValidateNumber(text):
    rs = re.search(".{2}\d{2}.{2}\d{4}", text)
    if rs is None:
        return None
    vehicleNumber =  rs.group()
    return vehicleNumber









#C:\Users\asus\AppData\Local\Tesseract-OCR

#tesseract_cmd = 'C:\\Users\\asus\\AppData\\Local\\Tesseract-OCR\\tesseract'

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\asus\\AppData\\Local\\Tesseract-OCR\\tesseract'
#TESSDATA_PREFIX= 'D:\Softwares\Tesseract-OCR'
tessdata_dir_config = '--tessdata-dir "C:\\Users\\asus\\AppData\\Local\\Tesseract-OCR\\tessdata"'


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

time.sleep(1)

while True:

    
    # Loop until the camera is working
    rval = False
    while(not rval):
        # Put the image from the webcam into 'frame'
        (rval, frame) = webcam.read()
        if(not rval):
            print("Failed to open webcam. Trying again...")
            exit(0)

    
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
        print("Yes")
        xd = (x2-x1)
        yd = (y2-y1)
        print("X:% Y:%i",xd,yd)
        if xd > 220 and yd >70:
            confirmation_count+=1
        else:
            confirmation_count = 0
            print("Size is small")
        
    else:
        
        confirmation_count = 0
        
        
    cv2.imshow('Number-Plate', resized_frame_copy)

    
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
            if reg_number is not None:
                time.sleep(3)
                
            confirmation_count = 0

    
    key = cv2.waitKey(1) & 0xFF
    
   
    
        
    if key == ord("q"):
        break
        
        
        
        
        
        
        
        
        
        
        
        
        