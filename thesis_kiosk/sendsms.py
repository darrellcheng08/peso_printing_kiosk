import serial
import RPi.GPIO as GPIO
import os, time

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(17, GPIO.OUT)
#GPIO.output(GPIO.LOW)
#time.sleep(13)

#Enable Serial Communication
port = serial.Serial("/dev/ttyAMAO", baudrate=9600, timeout=1)
#Transmetting AT Command

port.write('AT'+'\r\n')
rcv = port.read(10)
print(rcv)
time.sleep(1)

port.write('ATEO'+'\r\n')
#Disable the Echo
rcv = port.read(10)
print(rcv)
time.sleep(1)

port.write('AT+CMGF=1'+'\r\n')
#Select Message Format as text mode
rcv = port.read(10)
print(rcv)
time.sleep(1)

port.write('AT+CNMI=2,1,0,0,0'+'\r\n')
#New SMS Message Indecations
rcv = port.read(10)
print(rcv)
time.sleep(1)

#Sensing a message to a particular Number
port.write('AT+CMGS=09264668713'+'\r\n')
rcv = port.read(10)
print(rcv)
time.sleep(1)

port.write('Hello World'+'\r\n')
#Message
rcv = port.read(10)
print(rcv)


port.write("\x1A")
#Enable to send SMS
for in range(10):
	rcv = port.read(10)
	print(rcv)