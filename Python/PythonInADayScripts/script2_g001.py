import wx

class Frame(wx.Frame):

    # The exit fuction for exit button
    
    def exit(self, event):
        self.Destroy()

        
    # Added title parameter
    def __init__(self, title):
        #title = title variable

        wx.Frame.__init__(self, None, title=title, size=(300,200))

        # Cool stuff: Aligning the Window

        self.Center()

        self.Move((600,400))

        # Addinga button

        #First add panel. The panel is a container that groups things such as buttons and text

        # What is happening: 1. The button is being placed in the panel. 2. The Label is the text that appears on the button.
        # 3. The size is the size of the button. 4. The pos is the position of the button in the panel.
        
        panel = wx.Panel(self)

        button = wx.Button(panel, label="Exit", size=(100,40), pos=(100,30))


        #Bind button event ot he function self.exit

        # error comes out, so we need to create a function exit outside of the init function

        button.Bind(wx.EVT_BUTTON, self.exit)

        # Creating Menu Bar

        menuBar = wx.MenuBar()

        # Create the menus

        fileMenu = wx.Menu()

        editMenu = wx.Menu()

        self.SetMenuBar(menuBar)

        # so we never connected the fileMenu and editMenu to the menubar so here is the solution:

        # Add fileMenu and editMenu to menuBar

        menuBar.Append(fileMenu, "File")
        menuBar.Append(editMenu, "Edit")

        # Add items to fileMenu

        #Note change to "New File", the Create is a hover effect that occurs from self.CreateStatusBar()

        fileMenu.Append(wx.NewId(), "New File", "Create a new file")
        fileMenu.Append(wx.NewId(), "Open")
        exitItem = fileMenu.Append(wx.NewId(), "Exit")

        # Bind exit menu item to exit function
        
        self.Bind(wx.EVT_MENU, self.exit, exitItem)

        # Add items to editMenu

        editMenu.Append(wx.NewId(), "Don't")
        editMenu.Append(wx.NewId(), "Change")
        editMenu.Append(wx.NewId(), "Anything")

        #The Status Bar

        # Add functionality for when the user hovers over a menu item, a short description appears

        self.CreateStatusBar()

        # A static box can be used to group different widgets on the screen
    
        wx.StaticBox(panel, label='Static Box Title', pos=(10,10), size=(280,200))

        wx.StaticText(panel, label='Single line', pos=(100,100))


        # wx.ComboBox: aka drop down list, a combo box shows a list of items

        # here is how you can create your own:

        #simpsons =['Bart', 'Lisa', 'Maggie', 'Marge', 'Homer']

        #cb = wx.ComboBox(panel, pos=(100, 50), choices=simpsons)

app = wx.App()

#Pass in the frame title

frame = Frame("Python GUI")

frame.Show()

app.MainLoop()




        
