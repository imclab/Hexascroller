#!/usr/bin/python
import led_panel
from led_panel import panels, compile_image
from fontutil import base_font
from PIL import Image
import time
import signal
import sys
import threading

debug = False

class PanelThread(threading.Thread):
    def __init__(self, panel):
        pass

class ServiceThread:
    pass


if __name__=="__main__":

    if len(sys.argv) > 1 and sys.argv[1] == 'debug':
        debug = True

    led_panel.init(debug)
    panels[0].setRelay(True)
    
    def sigint_handler(signal,frame):
        print("Caught ctrl-C; shutting down.")
        panels[0].setRelay(False)
        led_panel.shutdown()
        sys.exit(0)
    signal.signal(signal.SIGINT,sigint_handler)

    while True:
        msg = time.strftime("%H:%M:%S")
        txtimg = base_font.strImg(msg)
        img = Image.new("1",(120,7))
        img.paste(txtimg,(15,0))
        img.paste(txtimg,(75,0))
        bitmap = compile_image(img,0,0)
            
        for j in range(3):
            panels[j].setCompiledImage(bitmap)
        time.sleep(0.1)

    panels[0].setRelay(False)

    led_panel.shutdown()
