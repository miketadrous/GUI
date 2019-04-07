from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setwarnings(False)

##LED
ledred = LED(14)
ledgreen = LED(15)
ledblue = LED(18)

##GUI
win=Tk()
win.title("LED Toggler")
myfont=tkinter.font.Font(family='Helvetica', size=12, weight="bold")

##Functions
def ledToggle():
    
    selection= str(color.get())
    
    if (selection=='red'):
        ledred.on()
        RedledButton["text"]="Red LED is On"
        ledgreen.off()
        GreenledButton["text"]="Turn Green LED on"
        ledblue.off()
        BlueledButton["text"]="Turn Blue LED on"
        

    elif (selection=='green'):
        ledgreen.on()
        GreenledButton["text"]="Green LED is On"
        ledred.off()
        RedledButton["text"]="Turn Red LED on"
        ledblue.off()
        BlueledButton["text"]="Turn Blue LED on"

    elif (selection=='blue'):
        ledblue.on()
        BlueledButton["text"]="Blue LED is On"
        ledred.off()
        RedledButton["text"]="Turn Red LED on"
        ledgreen.off()
        GreenledButton["text"]="Turn Green LED on"


def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
##initialize
color=StringVar()
color.set('red')
    
##Buttons
RedledButton=Radiobutton(win, text='Turn Red LED On', font = myfont, command=ledToggle,variable=color,value='red', bg='bisque2',height=1,width=24)
RedledButton.grid(row=0,column=1)

GreenledButton=Radiobutton(win, text='Turn Green LED On', font = myfont, command=ledToggle,variable=color,value='green', bg='bisque2',height=1,width=24)
GreenledButton.grid(row=1,column=1)

BlueledButton=Radiobutton(win, text='Turn Blue LED On', font = myfont, command=ledToggle,variable=color,value='blue', bg='bisque2',height=1,width=24)
BlueledButton.grid(row=2,column=1)

exitButton=Button(win, text='Exit', font = myfont, command=close, bg='red',height=1,width=6)
exitButton.grid(row=3,column=1)


ledToggle()

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()


