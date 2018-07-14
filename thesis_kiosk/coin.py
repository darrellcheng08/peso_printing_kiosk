import RPi.GPIO as GPIO
import time
import guizero
from guizero import App, warn, error, info
import sys

GPIO.setmode(GPIO.BCM)
counterPin=17
GPIO.setup(counterPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
counter = 1

fileName = sys.argv[1]
pages = sys.argv[2]
numcopy = sys.argv[3]

while True:
	input_state = GPIO.input(counterPin)
	if input_state == False:
		app = App(title="Printer Information")
		info("info", "Coin dropped "+ str(counter))
		app.display()
		time.sleep(0.1)
		counter += 1

		if int(counter) >= int(pages):
			change = counter - pages
			app = App(title="Printer Information")
			info("info", "Print Now!")
			info("info", "Your change is:" + change)
			app.display()
			subprocess.run(['python3', '/home/pi/printingkiosk/thesis_kiosk/print.py ' + fileName + pages + numcopy])
		elif int(counter) <= int(pages):
			app = App(title="Printer Information")
			info("info", "Kulang ang pera mu!")
			app.display()
		else:
			app = App(title="Printer Error")
			error("error", "Theres an error still something in print!")
			app.display()
			break  


