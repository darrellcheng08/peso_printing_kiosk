import subprocess
cmd = 'sudo hciconfig hci0 piscan'

subprocess.check_output(cmd, shell = True )

To allow the connection to complete you need to also do the following step to allow a remote device to actually connect with the pairing key 1234
sudo bluetooth-agent 1234

http://code.activestate.com/recipes/496837-count-pdf-pages/
https://www.quora.com/Which-Python-library-will-let-me-check-how-many-pages-are-in-a-PDF-file

os.system('libreoffice --writer file.odt')

If it is an odt file, you can open it just by
libreoffice file.odt

import serial
import RPi.GPIO as GPIO      
import os, time
 
GPIO.setmode(GPIO.BOARD)    
 
# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
 
# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
 
port.write('AT'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)
 
port.write('ATE0'+'\r\n')      # Disable the Echo
rcv = port.read(10)
print rcv
time.sleep(1)
 
port.write('AT+CMGF=1'+'\r\n')  # Select Message format as Text mode 
rcv = port.read(10)
print rcv
time.sleep(1)
 
port.write('AT+CNMI=2,1,0,0,0'+'\r\n')   # New SMS Message Indications
rcv = port.read(10)
print rcv
time.sleep(1)
 
# Sending a message to a particular Number
 
port.write('AT+CMGS="XXXXXXXXXX"'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)
 
port.write('Hello User'+'\r\n')  # Message
rcv = port.read(10)
print rcv
 
port.write("\x1A") # Enable to send SMS
for i in range(10):
    rcv = port.read(10)
    print rcv