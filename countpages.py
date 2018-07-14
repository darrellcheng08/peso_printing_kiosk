import PyPDF2
import subprocess
import os
import sys
#from win32com.client import Dispatch

num = 0
file = "D:/Desktop/printingkiosk/file/"+sys.argv[1]
file_extension = os.path.splitext(file)[1]

#subprocess.check_output(['libreoffice', '--convert-to', 'pdf', file])

if(file_extension == ".doc"):
	path = file.strip(".doc")+".pdf"
elif(file_extension == ".docx"):
	path = file.strip(".docx")+".pdf"
else:
	path = file

reader = PyPDF2.PdfFileReader(path)
num = reader.getNumPages()
print(num)

#COUNT PAGES IN .DOC AND .DOCX
# word = Dispatch('Word.Application')
# word.Visible = False
# word = word.Documents.Open('D:\Desktop\OJTDOCUMENTATION.doc')

# #get number of sheets
# word.Repaginate()
# num_of_sheets = word.ComputeStatistics(2)
# print(num_of_sheets)

