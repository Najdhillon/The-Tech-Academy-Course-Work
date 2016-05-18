import wx, db_program

class Frame(wx.Frame):

    def newCharacter(name, gender, age, occupation):

        # Changes: takes details as inputs

        print 'Adding a new character...'

    def addCharacter(self, event):
        
        pass

        name = self.sName.GetValue()
        gen = self.sGen.GetValue()
        age = self.sAge.GetValue()
        occ = self.sOcc.GetValue()

        print name
        print gen
        print age
        print occ

        db_program.newCharacter(name, gen, age, occ)
        print db_program.viewAll()

        # Fix for Empty Text Inputs

        # Checking if variables have a value

        if (name == '') or (gen == '') or (age == '') or (occ ==''):

            #Alert user that a variable is empty
            dlg = wx.MessageDialog(None, 'Some character details are missing. Enter values in each text box.','Missing Details',wx.OK)
            dlg.ShowModal()
            dlg.Destroy()

            return False

        # Rest after character has been added, fields cleared and age reset to zero
        # Empty text boxes when finsihed.

        self.sName.Clear()
        self.sGen.Clear()
        self.sOcc.Clear()

        #set the age back to zero

        self.sAge.SetValue(0)

        # Update list control: We are refreshing the table when a new character is added.. so we adding a call to the function fillListCtrl()

        self.fillListCtrl()


    def fillListCtrl(self):
        
        allData = db_program.viewAll()

        
        # Delete old data before adding new data. In order to avoid when new characters get added, other characters get added again to the list control

        self.listCtrl.DeleteAllItems()

        for row in allData:

            # Loop through and append data

            self.listCtrl.Append(row)

    def onSelect(self, event):

        # GET THE ID OF THE SELECTED ROW

        self.selectedID = event.GetText()

    # Creating the deleteCharacter() function

    def onDelete(self, event):

        # Delete the character

        db_program.deleteCharacter(self.selectedID)

        # Refresh the table

        self.fillListCtrl()
    
    def __init__(self,title):

        wx.Frame.__init__(self, None, title=title, size=(800,600))

        panel = wx.Panel(self)

        # Create menu bar

        menuBar = wx.MenuBar()

        fileMenu = wx.Menu()

        exitItem = fileMenu.Append(wx.NewId(), "Exit")

        menuBar.Append(fileMenu, "File")

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)

        self.CreateStatusBar()

        # Setup Add New Character UI

        # Text at the top

        wx.StaticBox(panel, label='Add a new character',pos=(20,40), size=(280,190))

        # Text for name, gender etc

        wx.StaticText(panel, label='Name: ', pos=(30,70))
        wx.StaticText(panel, label='Gender: ', pos=(30,110))
        wx.StaticText(panel, label='Age: ', pos=(30,150))
        wx.StaticText(panel, label='Occupation:', pos=(30,190))


        # Single line text boxes

        self.sName = wx.TextCtrl(panel, size=(150, -1), pos=(130,70))
        self.sGen = wx.TextCtrl(panel, size=(150, -1), pos=(130,110))

        # Fix for prevent in non-integer values  within the Age input field
        
        self.sAge = wx.SpinCtrl(panel, value='0', pos=(130, 150), size=(70,25))
        self.sOcc = wx.TextCtrl(panel, size=(150, -1), pos=(130,190))


        # Save button

        save = wx.Button(panel, label="Add Character", pos=(100,230))
        save.Bind(wx.EVT_BUTTON, self.addCharacter)

        # Using a table to show everything

        # Setup the Table UI
        # Setup table as listCtrl

        #wx.ListCtrl widget takes the size and position parameters.

        self.listCtrl = wx.ListCtrl(panel, size=(400,400), pos=(350,40), style=wx.LC_REPORT |wx.BORDER_SUNKEN)

        # Add column to listCtrl using InsertColumn() function. It uses two parameters

        #self. makes objects global

        self.listCtrl.InsertColumn(0, "ID")
        self.listCtrl.InsertColumn(1, "Name")
        self.listCtrl.InsertColumn(2, "Gender")
        self.listCtrl.InsertColumn(3, "Age")
        self.listCtrl.InsertColumn(4, "Occupation")

        # Inserting Data into the Table

        # Add data to the list control

        self.fillListCtrl()

        #Delete portion

        # Setup a delete button

        deleteBtn = wx.Button(panel, label="Delete", pos=(640,450))

        # Bind delete button to onDelete function

        deleteBtn.Bind(wx.EVT_BUTTON, self.onDelete)


        # Finding the character ID

        # Run onSelect function when item is selected

        self.listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelect)

        

    def exitProgram(self, event):
        self.Destroy()
    


app = wx.App()

frame = Frame("Some Text")

frame.Show()

app.MainLoop()


