import pyPdf
import os
import subprocess
output = subprocess.check_output(['libreoffice', '--convert-to', 'pdf' ,'test1.docx'])
os.path.abspath(output)
print(output)
reader = pyPdf.PdfFileReader(open("text.pdf"))
print (reader.getNumPages()) 
