import guizero
from guizero import App, PushButton, warn, info
import tkinter
import subprocess
import os

def cont():
	
	app.destroy()
	subprocess.run(['python3', '/home/pi/printingkiosk/thesis_kiosk/a.py'])

def admin():

	app = App(title="Administrator Information")
	info("info", "Hello Administrator")
	app.display()

app = App(title="WELCOME!", width=500, height=500, layout="auto")
button1 = PushButton(app, command=cont, text="Continue",  align="bottom")
button2 = PushButton(app, command=admin, text="Admin", align="bottom")                                                       
app.display()