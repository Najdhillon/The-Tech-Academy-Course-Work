
#Making a dictionary

epic_names_dict = {'Q-tip':'q@gmail.com',
                   'Phife Dawg':'p@gmail.com',
                   'Nas':'n@gmail.com'}


print epic_names_dict

#Adding numbers along with e-mails

epic_names_dict = {'q-tip':['q@gmail.com','444'],
                   'phife Dawg':['p@gmail.com','445'],
                   'nas':['n@gmail.com','446']}

#print epic_names_dict

#Retrieving back list of Q-tip back

#print epic_names_dict['Q-tip']

#Retrieving back the particular information of Q-tip

#Getting the email

#print epic_names_dict['Q-tip'][0]

#Getting the number back

#print epic_names_dict['Q-tip'][1]

#Entering a name, and getting an answer back

#personNames = raw_input("Who are you looking for?")

#personInfo = epic_names_dict[personNames]

#print personInfo

#Making it more user friendly

personNames = raw_input("Who are you looking for?").lower()

personInfo = epic_names_dict[personNames]



#print personInfo


#Adding in details for information regarding searchs

print "Here is their e-mail address:" + personInfo[0]

 
#Please note, the change that was made here involved changing the integers(numbers) within the dictionary and changing them from int to strings to avoid
# the issue of TypeError: cannot concatenate 'str' and 'int' objects

print "And their number is:" + personInfo[1]

# A different way doing the same thing
#Looks up the name in the epic dictionary




    # Creating a loop, so user can use program as many times as they want

#useApp = raw_input("Do you still want to use this program y/n?")

try:
    #Tries the following lines of texts, and if there are no errors then it runs

    personInfo = epic_programmer_dict[personsName]

    print 'Name:' + personsName.title()

    print 'Email:' + str(personInfo[0])

    print 'Number:' + str(personInfo[1])

except:

    #If there are errors, then this code gets run.

    print 'No information found for that name'
    

    

    
