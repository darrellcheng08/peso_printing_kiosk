import RPi.GPIO as GPIO
import time
import guizero
import sys

GPIO.setmode(GPIO.BCM)
counterPin=17
GPIO.setup(counterPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
counter = 1

for x in range(1, 50):
	input_state = GPIO.input(counterPin)
	if input_state == False:
		time.sleep(0.1)
		counter += 1
		break

print(counter)