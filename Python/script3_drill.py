import sqlite3

# Connecting to roster database

ctab = sqlite3.connect("roster.db")

# Creating table for database. PLEASE NOTE: if the table has already been created # out the statement

ctab.execute("CREATE TABLE ROSTER (ID INTEGER AUTOINCREMENT, NAME TEXT, SPECIES TEXT, IQ INT);")

# Protection from SQL injection

rosterValues = (('Jean-Baptiste Zorg','Human',122),('Korben Dallas','Meat Popsicle',100),('Ak\'not','Mangalore',-5))
