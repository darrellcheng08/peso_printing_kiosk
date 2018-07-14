import subprocess
import sys
import os

subprocess.call(['libreoffice', '--view','--writer', '/var/www/html/printingkiosk/file/'+sys.argv[1]])

subprocess.check_call(['libreoffice', '--impress', '/var/www/html/printingkiosk/file/'+sys.argv[1]])
os.system('libreoffice --show /var/www/html/printingkiosk/file/'+sys.argv[1])

#convert docx to pdf
os.system('libreoffice --convert-to pdf /var/www/html/printingkiosk/file/'+sys.argv[1])