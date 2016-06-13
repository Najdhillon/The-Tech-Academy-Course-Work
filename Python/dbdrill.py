
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil, os, time, sqlite3, datetime

conn = sqlite3.connect('recentmodcheck.db')
c = conn.cursor()

def createTab():

    c.execute("CREATE TABLE if not exists recentmod(ID Integer Primary Key Autoincrement,Dates INT)") 
    
createTab()

def attt():

    u = time.time()
    date = str(datetime.datetime.fromtimestap(u).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO recentmod(Dates) VALUES(?)",(date))
    conn.commit()

    


def addSource() :
        global sdirect
        sdirect = filedialog.askdirectory()
        #return sdirect

def addDest() :
        global ddirect
        ddirect = filedialog.askdirectory()
        #return ddirect

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
                        print('{} has been copied to {}'.format(src,dest)

                        

##                        u = time.time()
##                        date = str(datetime.datetime.fromtimestap(u).strftime('%Y-%m-%d %H:%M:%S'))
##                        c.execute("INSERT INTO recentmod(Dates) VALUES(?)",(date))
##                        conn.commit()
##                        conn.close()
##                        c.close()

    

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




root = makeWindow()
root.mainloop()

