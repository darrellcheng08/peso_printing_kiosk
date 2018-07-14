import mysql.connector
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

con = mysql.connector.connect(user='root', password='',
	host='127.0.0.1',
	database='alarmdb')
cursor = con.cursor()

def insert_mobile():
	try:
		cursor.execute("INSERT INTO mobilelist(mobileno)VALUES('"+mobileno.get()+"')")
		con.commit()
		loadnumber()
	except:
		con.rollback()

def delete(event):
			item = tv.identify('item',event.x,event.y)
			sid = tv.item(item,"text")
			result = messagebox.askyesno("Delete","Are you sure you want to delete this record?")
			if result == True:
				try:
					cursor.execute("DELETE FROM mobilelist where id='"+sid+"'")
					con.commit()
					loadnumber()
				except:
					con.rollback()
				else:
					print("I'm Not Deleted Yet")
	#tv.item(item,"values")

def loadnumber():
		tv.delete(*tv.get_children())
		cursor.execute("SELECT * FROM mobilelist")
		for user in cursor:
			tv.insert('', 'end', text=str(user[0]), values=(user[1]))
			tv.bind("<Button-1>", delete)

master = Tk()
tv = Treeview()
#start label mobile number
Label(master, text="Number of Bond Paper: ").grid(row=0,column=0,sticky=W, padx=(10, 10))
mobileno = Entry(master)
mobileno.grid(row=0, column=0, sticky=W, padx=140, pady=0)

btnsave = Button(master, text='Add Number', command=insert_mobile).grid(row=1, column=0, sticky=W, padx=(10, 0))
btndelete = Button(master, text='Delete', command=delete).grid(row=1, column=0, sticky=W, padx=(100, 0))
#end label mobile number

#start table
tv['columns'] = ('mobileno')
tv.heading("#0", text='ID', anchor='center')
tv.column("#0", anchor="w", width=40)
tv.heading('mobileno', text='Number of Bond Paper')
tv.column('mobileno', width=300, anchor='center')
tv.grid(row=2, column=0)
tv.grid(padx=10, pady=10)

loadnumber()
mainloop( )