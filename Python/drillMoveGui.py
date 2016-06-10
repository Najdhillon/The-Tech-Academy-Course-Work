<<<<<<< Updated upstream
import wx, shutil, os, time
from datetime import datetime, timedelta

=======
import wx, time, shutil, os
from datetime import datetime, timedelta
>>>>>>> Stashed changes

class Frame(wx.Frame):
   
    def __init__(self, title):
       
        wx.Frame.__init__(self,None, title=title, size =(350,250))
        panel = wx.Panel(self)

        button1 = wx.Button(panel, label='Choose', size=(100,40),pos=(100,30))
        button2 = wx.Button(panel, label='Choose', size=(100,40),pos=(100,95))
        button3 = wx.Button(panel, label='Begin', size=(100,40),pos=(50,150))
        button4 = wx.Button(panel, label='Exit', size=(100,40),pos=(190,150))

        button1.Bind(wx.EVT_BUTTON, self.onDirSource)
        button2.Bind(wx.EVT_BUTTON, self.onDirDest)
        button3.Bind(wx.EVT_BUTTON, self.executeCopy)
        button4.Bind(wx.EVT_BUTTON, self.exit)
       
       
        wx.StaticText(panel, label='Choose your Source:', pos=(100,10))
        wx.StaticText(panel, label='Choose your Destination:', pos=(94,73.5))

    # Method for opening the file directory to select source folder
        
    def onDirSource(self, event):

        dlg = wx.DirDialog(None, "Choose a folder:",
                           style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            srcf = dlg.SetPath()

        return srcf
        dlg.Destroy()

    # Method for opening the file directory to select destination folder        


    def onDirDest(self, event):


        dlg = wx.DirDialog(None, "Choose a folder:",
                           style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            dstf = dlg.SetPath()
            
        return dstf

        dlg.Destroy()

    def executeCopy(self, event):

<<<<<<< Updated upstream
        srcf = onDirSource()
        destf = onDirDest()

        src = os.path.join(srcf,f)
        dest = os.path.join(destf,f)
    
        if f.endswith(".txt"):
=======
        srcf = self.onDirSource()
        destf = self.onDirDest()

        #srcf = ('C:\\Users\\navjot.dhillon\\Desktop\DailyFile\\')
        #destf = ('C:\\Users\\navjot.dhillon\\Desktop\MoveFile\\')

        for f in os.listdir(srcf):

            src = os.path.join(srcf,f)
            dest = os.path.join(destf,f)
            
            if f.endswith(".txt"):

                # Last Mod time calculation

                modtime = time.time() - (os.path.getmtime(src))
>>>>>>> Stashed changes

            # Last Mod time calculation

<<<<<<< Updated upstream
            modtime = time.time() - (os.path.getmtime(src))

            #modtimets = (datetime.fromtimestamp(modtime)) - this was not working(ND)

            h24ago = time.time() - (24*60*60)

            last24 = time.time() - h24ago
            
            #check = modtime - timedelta(hours = 24)

            if modtime < last24:

                    shutil.copy(src, dest)
                    print '{} has been copied to {}'.format(src,dest)
            
=======
                h24ago = time.time() - (24*60*60)

                last24 = time.time() - h24ago
                
                #check = modtime - timedelta(hours = 24)

                if modtime < last24:

                        shutil.copy(src, dest)
                        print '{} has been copied to {}'.format(src,dest)
        
>>>>>>> Stashed changes

    # Method for exit   

    def exit(self,event):
        self.Destroy()   
       
app = wx.App()
frame = Frame("File Transfer")
frame.Show()
app.MainLoop()
