
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil, os, time, sqlite3,datetime



def addSource() :
        global sdirect
        sdirect = filedialog.askdirectory()
        return sdirect

def addDest() :
        global ddirect
        ddirect = filedialog.askdirectory()
        return ddirect


conn = sqlite3.connect('drilldb.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS addStuff(ID INTEGER PRIMARY KEY AUTOINCREMENT, modtime INTEGER)')

def dynamic_data_entry():

    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO addSTUFF (modtime) VALUES (?)", (date,))

    conn.commit()

def beginCopy() :
        
        srcf = sdirect
        destf = ddirect

        for f in os.listdir(srcf):

            src = os.path.join(srcf,f)
            dest = os.path.join(destf,f)
            
            if f.endswith(".txt"):

                # Last Mod time calculation

                modtime = time.time() - (os.path.getmtime(src))

                #modtimets = (datetime.fromtimestamp(modtime)) - this was not working(ND)

                h24ago = time.time() - (24*60*60)

                last24 = time.time() - h24ago
                
                #check = modtime - timedelta(hours = 24)

                if modtime < last24:

                        shutil.copy(src, dest)
                        print('{} has been copied to {}'.format(src,dest))
                        dynamic_data_entry()

    
    
def makeWindow () :
    global root    
    root = Tk()

    frame1 = Frame(root)
    frame1.pack()

    Label(frame1, text="Choose your Source").grid(row=0, column=0, sticky=W)
    
    b1 = Button(frame1,text="Choose",command=addSource)
    b1.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Choose your Destination").grid(row=1, column=0, sticky=W)

    b2 = Button(frame1,text="Choose",command=addDest)
    b2.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Begin Check for files").grid(row=2, column=0, sticky=W)

    b3 = Button(frame1,text="Start",command=beginCopy)
    b3.grid(row=2, column=1, sticky=W)

    Label(frame1, text="Last File Check:").grid(row=3, column=0, sticky=W)

    c.execute("SELECT MAX(modtime) FROM addStuff")
    date = c.fetchall()

    Label(frame1, text=date).grid(row=3, column=1, sticky=W)





root = makeWindow()
root.mainloop()

