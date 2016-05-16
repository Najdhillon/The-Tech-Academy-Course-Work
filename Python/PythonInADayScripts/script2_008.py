import wx

class Frame(wx.Frame):

    #Added title parameter

    def __init__(self, title):
        # title = title variable

        wx.Frame.__init__(self, None, title=title, size=(300,200))

        panel = wx.Panel(self)

        #wx.StaticBox - A static box can be used to group different widgets on the screen.

        #wx.StaticBox(panel, label='Static Box Title', pos=(10,10), size=(280,200))

        #wx.StaticText - Static text can be added like so:

        #wx.StaticText(panel, label='Single line', pos=(100,100))

        #wx.ComboBox aka drop down list - A combo box shows a list of items. Here is how you can create your own:

        #simpsons =['Bart', 'Lisa', 'Maggie', 'Marge', 'Homer']

        # NOTE: style=wx.CB_READONLY was added to prevent the text from being edited

        #cb = wx.ComboBox(panel, pos=(100,50), choices=simpsons, style=wx.CB_READONLY)

        # Adding Checkboxes

        # wx.CheckBox(panel, label='Male', pos=(100,50))
        
        # wx.CheckBox(panel, label='Female', pos=(100,80))

        # Adding RadioButton

        #wx.RadioButton(panel, label='Male', pos=(100,50), style=wx.RB_GROUP)

        #wx.RadioButton(panel, label='Female', pos=(100,80), style=wx.RB_GROUP)

        # wx.TextCtrl Adding input fields
        # The value "-1" has been used as the height to sst the text control at the default height. Allows to change the width and keep the default height

        #wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(300,200), pos=(100,50))

        # Spin Control: allows you to increment and decrement numbers

        wx.SpinCtrl(panel, value='0', pos=(130, 50), size=(70, 25))
        

app = wx.App()

# Pass in the frame title

frame = Frame("Python GUI")

frame.Show()

app.MainLoop()

