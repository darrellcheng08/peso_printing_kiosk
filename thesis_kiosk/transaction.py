import RPi.GPIO as GPIO
import sched, time
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
global credit
global counter

app = App(title="Transaction Form", width=500, height=500, layout="auto")

filename = ""
pages = 0
pages=reader.getNumPages()

file_name=Text(app, text="File Name: " + filename) 
nopages=Text(app, text="Number of Page(s): " + str(pages))
text2=Text(app, text="Credits:")
text3=Text(app, text="Number of Copies: ") 
copies=TextBox(app)
btnprint = PushButton(app, text="Print")
app.display()

s = sched.scheduler(time.time, time.sleep)
def load_credits(sc): 
    print("loading of credits here")

s.enter(60, 1, load_credits, (s,))
s.run()
