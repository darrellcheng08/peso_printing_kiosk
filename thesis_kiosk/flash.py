#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import guizero
from guizero import App, PushButton, Text, TextBox, info, warn
import tkinter
import tkinter.filedialog
from tkinter.filedialog import askopenfilename
import os
import subprocess
from docx import Document
import PyPDF2
import cups
global num
global file
num = 0

def brow():
  file = tkinter.filedialog.askopenfilename()

  btnpreview.show()
  btnprint.show()
  lblnumcopy.show()
  credits.show()	
  copies.show()
  brow.show()
  brow.value = file
  file = brow.value
  file_extension = os.path.splitext(file)[1]

  output = subprocess.check_output(['libreoffice', '--convert-to', 'pdf', brow.value])

  if(file_extension == ".doc"):
    path = file.strip(".doc")
  elif file_extension == ".pdf":
    path = file.strip(".pdf")
  else:
    path = file.strip(".docx")

    reader = PyPDF2.PdfFileReader(path+".pdf")
    numpage.value=reader.getNumPages()

    numpage.show()
    num = numpage.value

def prev():

    subprocess.call(['libreoffice', '--view','--writer', brow.value])

def prin():

    os.system('python /home/pi/printingkiosk/thesis_kiosk/coin.py ' + file + ' ' + str(num) + ' ' + str(copies.value))   	

s = sched.scheduler(time.time, time.sleep)
def load_credits(sc): 
    app = App(title="Coin Information")
    info("info", "Coin dropped")
    app.display()
s.enter(60, 1, load_credits, (s,))
s.run()

app = App(title="FLASH DRIVE", width=500, height=500, layout="auto")
button1 = PushButton(app, command=brow, text="Browse File", align="right")
brow = Text(app, text = "")
brow.hide()
btnpreview = PushButton(app, command=prev, text="Preview File", align="right")
btnpreview.hide()
btnprint = PushButton(app, command=prin, text="Print File", align="right")
btnprint.hide()
credits = Text(app, text="Credits: ")
credits.hide()
numpage= Text(app,text="")
numpage.hide()
text3=Text(app, text="")
lblnumcopy=Text(app, text="Number of Copies: " + numpage.value) 
lblnumcopy.hide()
copies=TextBox(app)
copies.hide()
app.display()
