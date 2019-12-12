
# http://tanksw.com/piano-tiles/

import numpy
from PIL import ImageGrab, ImageOps
import pyautogui
import time


class cor():
    againbtn = (603, 785)
    
    point1 = (330,600)
    point2 = (430,600)
    point3 = (530,600)
    point4 = (630,600)
    
    box1 = (point1[0], point1[1],point1[0]+2, point1[1]+2)
    box2 = (point2[0], point2[1],point2[0]+2, point2[1]+2)
    box3 = (point3[0], point3[1],point3[0]+2, point3[1]+2)
    box4 = (point4[0], point4[1],point4[0]+2, point4[1]+2)
      
def again():
    pyautogui.click(cor.againbtn)
    

def clickgen(pointema):
    pyautogui.click(pointema)
    
def imggrab(boxema):
    gimage = ImageOps.grayscale(ImageGrab.grab(boxema))
    a = numpy.array(gimage.getcolors())
    return(a.sum())
    
while True: 
    if(imggrab(cor.box1) == 23):
        clickgen(cor.point1)
        
    if(imggrab(cor.box2) == 23):
        clickgen(cor.point2)
        
    if(imggrab(cor.box3) == 23):
        clickgen(cor.point3)
        
    if(imggrab(cor.box4) == 23):
        clickgen(cor.point4)
        
