# Step one: Create the table

import sqlite3

# Connect to simpsons database

conn = sqlite3.connect('simpson.db')

#Outputting the data. Make a function that needs to take in an array as parameter and then loop through each row to print out the data

def printData(data):
    for row in data:
        print "Id:",row[0]
        print "Name:",row[1]
        print "Gender:",row[2]
        print "Age:",row[3]
        print "Occupation:",row[4]
        

def createTable():

    conn.execute("CREATE TABLE if not exists SIMPSON_INFO(ID Integer Primary Key Autoincrement, Name Text, Gender Text, Age Int, Occupation Text);")

createTable()


# Step two: Adding Characters to the Database

# User Inputs

def newCharacter():

    print 'Adding a new character...'

    #Take inputs

    name = raw_input('Name: ')
    gender = raw_input('Gender: ')
    age = raw_input('Age: ')
    occupation = raw_input('Occupation: ')


    #Back to SQL: using the .format for inputting variables into strins

    # Create values part of sql command
    
    val_str = "'{}','{}','{}','{}'".format(name, gender, age, occupation)

    #print val_str

    sql_str = "INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION) VALUES ({});".format(val_str)

    #print sql_str

    conn.execute(sql_str)
    conn.commit()

    #print "Number of changes:", conn.total_changes

    

#newCharacter()

    

# Step three: Viewing all characters

# Make a function that collects the data from the table and prints it out. The function will be called viewALL() and look like the following:

def viewAll():
    
    #Create sql string
    sql_str = "Select * from SIMPSON_INFO"
    cursor = conn.execute(sql_str)

    # Display the data by using .fetchall() and then printing the result

    # Get data from cursor in array

    rows = cursor.fetchall()

    print rows



#viewAll()

    
#Step Four: Viewing Specific Characters

# We can also make a function that searches for a specific character and then prints out their details



#Break down how the function will work: 1. Ask user for hte character name, 2.Run SQL statement using this name

#4. Output results of statement

# Asking user for the Character Name

def viewDetails():
    
    print "Viewing character details"

    #Take name input

    name = raw_input("Enter the character's name: ")

    #print name


    #SQL statement

    sql_str = "SELECT * from SIMPSON_info where NAME ='{}'".format(name)

    #print sql_str

    cursor = conn.execute(sql_str)

    #Get data in array form

    rows = cursor.fetchall()
    
    #print printData(rows)

    #If a user is not found

    if len(rows) == 0:
        #There is no data in array
        print 'No records found'
    else:
        #print the data

        printData(rows)



#viewDetails()


#STEP FIVE: Delete a character
# We are going to make a function that deletes a character. Here is how it will work: 1. Ask user for the charactername. 2. Run SQL statement using this name
# 3. Output results of statement 4. Confirm the delete 5. Run delete SQL

#Reusing Code
# Using the similar functionality to the viewDeatils() function

def deleteCharacter():
    print "Deleting a Character"

    # Take  name input
    name = raw_input("Enter the character's name: ")
    sql_str = "SELECT * from SIMPSON_INFO where NAME = '{}'".format(name)

    cursor = conn.execute(sql_str)

    # Get data in array form

    rows = cursor.fetchall()

    # ID to change
    change_id = 0

    if len(rows) == 0:
        # There is no data in array

        print 'No records found'

        # End the function

        return
    
    elif len(rows) == 1:

        print 'One record found'

        # Select row

        row = rows[0]

        # Select Id
        
        change_id = row[0]
        printData(rows)
        

    else:

        print 'More than one record found...'

        printData(rows)

        change_id = raw_input('Type the ID of the character to update: ')


    print "Change ID:", change_id

    delete = raw_input("Confirm character delete(y/n): ")

    #Deleting the character: confirmation

    if delete == "y":

        sql_str = "DELETE from SIMPSON_INFO where ID = {}".format(change_id)

        conn.execute(sql_str)

        conn.commit()

        print "Number of changes: ", conn.total_changes
        
#deleteCharacter()

# Putting it all Together
# create a user interface that makes it wasy for the user to add, view, and delete a character

def options():

    # Print out the options

    print 'What would you like to do?'
    
    print '1. Add a new character'
    
    print '2. View all characters'
    
    print '3. Search for a character'
    
    print '4. Delete a character'
    
    print '5. Exit'

    #Ask user what they want to do
    response = raw_input('Enter number: ')

    if response == '1':

        newCharacter()

    elif response == '2':
    

        viewAll()

    elif response == '3':

        viewDetails()

    elif response == '4':

        deleteCharacter()

    else:

        print 'Exiting the program'

        return

               
def mainLoop():

    in_loop = True
    
    while in_loop == True:

        # Run options function

        options ()

        #Ask user if they want to continue

        again = raw_input('Would you like to do something else? (y/n)')

        # if answer does not equal 'y', exit loop

        if again != 'y':
            
            in_loop = False

mainLoop()
