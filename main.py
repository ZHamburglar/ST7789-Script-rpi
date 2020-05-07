#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import sys
import os
import psutil
import datetime
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
from waveshare_2inch_LCD import ST7789
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.INFO)

dateString = '%Y/%m/%d %H:%M:%S'

print(datetime.datetime.now().strftime(dateString))
def my_function():
  print("Hello from a function")

my_function()

# % Ram Usage with psutil
def get_ram_info():
    """ Return RAM usage using psutil """
    ram_cent = psutil.virtual_memory()[2]
    return str(ram_cent)

# CPU Temp in Celsius
def get_cpu_tempfunc():
    """ Return CPU temperature """
    result = 0
    mypath = "/sys/class/thermal/thermal_zone0/temp"
    with open(mypath, 'r') as mytmpfile:
        for line in mytmpfile:
            result = line

    result = float(result)/1000
    result = round(result, 1)
    return str(result)

def get_gpu_tempfunc():
    """ Return GPU temperature as a character string"""
    res = os.popen('/opt/vc/bin/vcgencmd measure_temp').readline()
    return res.replace("temp=", "")


def get_cpu_use():
    """ Return CPU usage using psutil"""
    cpu_cent = psutil.cpu_percent()
    return str(cpu_cent)

print(get_ram_info())
print('j',get_cpu_tempfunc())
print('CPU Use:',get_cpu_use())
print('GPU Temp:',get_gpu_tempfunc())

disp = ST7789.ST7789()
# Initialize library.
disp.Init()

# Clear display.
disp.clear()

while True:
    print ("2inch LCD Module")


    # image = Image.new('RGB', (disp.width,disp.height), (255,255,255)) 
    image = Image.new('RGB', (disp.height,disp.width), (0,0,0)) 

    draw = ImageDraw.Draw(image)

    font30 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 30)
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    print ("***draw line")
    draw.line([(40,20),(200,20)], fill = "BLUE",width = 5)
    draw.line([(40,20),(40,200)], fill = "BLUE",width = 5)
    draw.line([(40,200),(200,200)], fill = "BLUE",width = 5)
    draw.line([(200,20),(200,200)], fill = "BLUE",width = 5)
    print ("***draw rectangle")
    draw.rectangle([(50,30),(190,70)],fill = "BLUE")
    
    print ("***draw text")
    draw.text((60,30), u'Boot Program', font = font30, fill = "WHITE")
    draw.text((50, 75), 'Waveshare Electronic ', font = font15, fill = "BLUE")
    draw.text((75, 110), '2.0inch LCD ', font = font15, fill = "BLUE")
    draw.text((72, 140), 'Test Program ', font = font15, fill = "BLUE")
    time.sleep(.1)
    draw.text((72, 170), datetime.datetime.now().strftime(dateString), font = font15, fill = "BLUE")


    image=image.rotate(180) 
    disp.ShowImage(image)

    # read bmp file 
    # bmp = Image.open(os.path.join(picdir, 'LCD_2inch.bmp'))	
    # image.paste(bmp, (0,0))  
    # image=image.rotate(180)
    # disp.ShowImage(image)
    time.sleep(1)






# except KeyboardInterrupt:    
#     logging.info("ctrl + c:")
#     exit()

