from guizero import App, PushButton
import tkinter
import os
import subprocess

def back():
    choose.destroy()
    subprocess.run(['python3', '/home/pi/printingkiosk/thesis_kiosk/thesis.py'])

def flashd():
    choose.destroy()
    subprocess.run(['python3', '/home/pi/printingkiosk/thesis_kiosk/flash.py'])
    
choose = App(title="PRINTING KIOSK", width=500, height=100, layout="grid")
button1 = PushButton(choose, command=flashd, text="Flash Drive",grid=[1,1],align="bottom")
button2 = PushButton(choose, command="", text="Bluetooth", grid=[2,1],align="bottom")
button3 = PushButton(choose, command=back, text="Cancel", grid=[3,1],align="bottom")                                                          
choose.display()
