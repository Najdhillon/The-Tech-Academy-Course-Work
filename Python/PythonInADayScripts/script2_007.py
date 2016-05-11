import wx

# wx.App() creates the application object. This is required for every program you make using wxPython

app = wx.App()

# wx.Frame() creates a window. Like every other window you use

frame = wx.Frame(None, title="Python GUI", size=(300,200))

#.Show() makes the frame appear on the screen.

frame.Show()

# .MainLoop handles all the evens such as clicking or scrolling

app.MainLoop()


