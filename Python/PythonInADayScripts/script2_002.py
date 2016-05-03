# wx Widgets

import wx

# These are some of the most commonly used widgets

# wx.StaticText: static text can be added like so:


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Python GUI", size(300,200))



        wx.StaticText(panel, label='Single Line', pos=(100,100))


        # A static box can be used to group different widgets on the screen

        wx.StaticBox(panel, label='Static Box Title', pos=(10,10), size=(280,200))

        wx.StaticText(panel, label='Single line', pos=(100,100))


        # wx.ComboBox: aka drop down list, a combo box shows a list of items

        # here is how you can create your own:

        simpsons =['Bart', 'Lisa', 'Maggie', 'Marge', 'Homer']

        cb = wx.ComboBox(panel, pos=(100, 50), choices=simpsons)

app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()

