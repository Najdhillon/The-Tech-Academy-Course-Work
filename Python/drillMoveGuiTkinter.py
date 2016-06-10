
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def addSource () :
        sdirectory.set(filedialog.askdirectory())
        return

def addDest() :

        ddirectory.set(filedialog.askdirectory())
        return

def beginCopy() :
    del phonelist[whichSelected()]
    setSelect ()

def exitApp  () :
    name, phone = phonelist[whichSelected()]
    nameVar.set(name)
    phoneVar.set(phone)

def makeWindow () :
        
    global sdirectory, ddirectory

    root = Tk()

    frame1 = Frame(root)
    frame1.pack()

    sdirectory = StringVar()
    ddirectory = StringVar()

    Label(frame1, text="Choose your Source").grid(row=0, column=0, sticky=W)
    
    b1 = Button(frame1,text="Choose",command=addSource)
    b1.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Choose your Destination").grid(row=1, column=0, sticky=W)

    b2 = Button(frame1,text="Choose",command=addDest)
    b2.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Begin Check for files").grid(row=2, column=0, sticky=W)

    b3 = Button(frame1,text="Start",command=beginCopy)
    b3.grid(row=2, column=1, sticky=W)

    b4 = Button(frame1,text="Exit",command=exitApp)
    b4.grid(row=3, column=1, sticky=W)



root = makeWindow()
root.mainloop()

