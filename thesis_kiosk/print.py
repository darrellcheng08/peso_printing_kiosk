import cups
import sys
from guizero import App, warn
import subprocess

conn = cups.Connection()
printers = conn.getPrinters()
cups.setUser('pi')
fileName = sys.argv[1]
pages = sys.argv[2]
numcopy = sys.argv[3]

totalpages = numcopy * pages;
i = 0
for printer in printers:
	print (printer, printers[printer]["device-uri"])
	printer_name=printers.keys()[0]
	printqueuelength = len(conn.getJobs())

	while(i<totalpages):
		if(printqueuelength > 1):
      subprocess.run(['python3', '/home/pi/printingkiosk/sendsms.py'])   
      app = App(title="Printer Error")
      error("error", "Theres an error still something in print!")
      app.display()
    else:
     conn.printFile(printer_name, fileName, " ", {})
     i+=1

#Include php in python
# def php(script_path):
#     p = subprocess.Popen(['php', script_path], stdout=subprocess.PIPE)
#     result = p.communicate()[0]
#     return result

# # YOUR CODE BELOW:
# page_html = "<h1>News and Updates</h1>"
# news_script_output = php("news-generator.php") 
# print page_html + news_script_output


