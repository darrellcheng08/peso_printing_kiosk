#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import guizero
from guizero import App, PushButton, Text, TextBox, info, warn
import tkinter
import tkinter.filedialog
from tkinter.filedialog import askopenfilename
import os
import subprocess
import PyPDF2
global credit

def brow():
  global counter
  global page
  global num
  global file
  page = 0
  credit = 0
  num = 0
  file = tkinter.filedialog.askopenfilename()

  btnpreview.show()
  btnprint.show()
  lblnumcopy.show()	
  copies.show()
  brow.show()
  brow.value = file
  file = brow.value

  output = subprocess.check_output(['libreoffice', '--convert-to', 'pdf' ,'test1.docx'])

  path = file.strip(".docx")

  reader = PyPDF2.PdfFileReader(path+".pdf")
  text2.value = reader.getNumPages()

  text2.show()
  num = text2.value

def prev():

  subprocess.call(['libreoffice', '--view','--writer', brow.value])

def prin():

  subprocess.run(['python', '/home/pi/print.py'+ num])

app = App(title="FLASH DRIVE", width=500, height=500, layout="auto")
button1 = PushButton(app, command=brow, text="Browse File", align="right")
brow = Text(app, text = "")
brow.hide()
btnpreview = PushButton(app, command=prev, text="Preview File", align="right")
btnpreview.hide()
btnprint = PushButton(app, command=prin, text="Print File", align="right")
btnprint.hide()
text1 = Text(app, text="")
text1.hide()
text2= Text(app,text="")
text2.hide()
text3=Text(app, text="")
lblnumcopy=Text(app, text="Number of Copies: ") 
lblnumcopy.hide()
copies=TextBox(app)
copies.hide()

app.display()
