import tkinter

#create main window
master = tkinter.Tk()
master.title("tester")
master.geometry("300x100")


#make a label for the window
label1 = tkinter.Label(master, text='Hellooooo')
# Lay out label
label1.pack()

# Run forever!
master.mainloop()
