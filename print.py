import cups
import sys
from guizero import App, warn

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
            app = App(title="Printer Error")
            error("error", "Theres an error still something in print!")
            app.display()
        else:
           conn.printFile(printer_name, fileName, " ", {})
           i+=1

