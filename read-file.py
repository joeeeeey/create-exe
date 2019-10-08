from tkinter import filedialog
from tkinter import *

root = Tk()

canvas1 = Canvas(root, width = 400, height = 400)
canvas1.pack()


def drag_file():
	root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))
	print(root.filename)

	label1 = Label(root, text= 'Hello World!', fg='green', font=('helvetica', 12, 'bold'))
	canvas1.create_window(150, 200, window=label1)
    
button1 = Button(text='Select .xlsx file',command=drag_file, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)


root.mainloop()