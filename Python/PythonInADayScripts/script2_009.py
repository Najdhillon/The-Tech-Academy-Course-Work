import wx

class Frame(wx.Frame):

    def spinControl(self,event):

        # Get spin control value

        #event.GetPosition() function looks up the current value in the spin control. The label of self.valueText was then set to this value

        value = event.GetPosition()

        # Update static text

        self.valueText.SetLabel(str(value))
        

    def __init__(self,title):

        wx.Frame.__init__(self, None, title=title, size=(300,200))

        panel = wx.Panel(self)

        # Used self.valueText to make the static text a global variable. This means
        # we can access the static text in other functions

        sc = wx.SpinCtrl(panel, value='0', pos=(130, 50), size=(70,25))

        self.valueText = wx.StaticText(panel, label='', pos=(130,80))

        # bind the spin control to run a function when its value has changed. The function will be called self.spinControl:

        sc.Bind(wx.EVT_SPINCTRL, self.spinControl)


app = wx.App()

frame = Frame("Some Text")

frame.Show()

app.MainLoop()
