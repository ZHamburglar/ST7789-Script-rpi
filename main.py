#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import sys
import os
import subprocess

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
from waveshare_2inch_LCD import ST7789
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.INFO)


try:
    print ("2inch LCD Module")
    disp = ST7789.ST7789()
    # Initialize library.
    disp.Init()
    WIDTH = disp.width
    HEIGHT = disp.height
    print ('Width: ', WIDTH, '  Height: ', HEIGHT)

    # Clear display.
    disp.clear()

    # image = Image.new('RGB', (disp.width,disp.height), (255,255,255))
    # White Background 
    image = Image.new('RGB', (disp.height,disp.width), (255,255,255)) 
    # Black Background
    image = Image.new('RGB', (disp.height,disp.width), (0,0,0)) 

    draw = ImageDraw.Draw(image)

    font30 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 30)
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    print ("***draw line")
    # Top Side
    draw.line([(10,10),(310,10)], fill = "BLUE",width = 5)
    # Left side
    draw.line([(10,10),(10,230)], fill = "BLUE",width = 5)
    # Bottom Side
    draw.line([(10,230),(310,230)], fill = "BLUE",width = 5)
    # Right Side
    draw.line([(310,10),(310,230)], fill = "BLUE",width = 5)
    print ("***draw rectangle")
    draw.rectangle([(50,30),(190,70)],fill = "BLUE")
    
    bold = 'boooot'

    # Device IP Address
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = "IP: "+subprocess.check_output(cmd, shell=True).decode("utf-8")

    cmd = "pidof hostapd | wc -l | awk '{printf \"Hotspot: %s\", $1 == 1 ? \"Active\" : \"Down\"}'"
    Hostapd = subprocess.check_output(cmd, shell=True).decode("utf-8")

    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")

    cmd = "free -m | awk 'NR==2{printf \"Mem: %sMB %.2f%%\", $3,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")

    cmd = "cat /sys/class/thermal/thermal_zone0/temp |  awk \'{printf \"CPU Temp: %.1f C\", $(NF-0) / 1000}\'" # pylint: disable=line-too-long
    Temp = subprocess.check_output(cmd, shell=True).decode("utf-8")

    print (IP)
    print (MemUsage)
    # print ("***draw text")
    draw.text((60,30), bold, font = font30, fill = "WHITE")
    draw.text((50, 75), 'Waveshare Electronic ', font = font15, fill = "BLUE")
    draw.text((75, 110), '2.0inch LCD ', font = font15, fill = "BLUE")
    draw.text((72, 140), 'Test Program ', font = font15, fill = "BLUE")
    draw.text((72, 170), Temp, font=font15, fill="#550000")


    image=image.rotate(180) 
    disp.ShowImage(image)
    time.sleep(3)

    # read bmp file 

    # bmp = Image.open(os.path.join(picdir, 'machomadness.png'))	
    # image.paste(bmp, (0,0))  
    # image=image.rotate(180)
    # disp.ShowImage(image)

except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    exit()

