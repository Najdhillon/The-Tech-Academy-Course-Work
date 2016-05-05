import sqlite3

rosterValues = (('Jean-Baptistse Zorg','Human',122),('Korben Dallas','Meat Popsicle',100),('Ak\'not','Mangalore','-5'))

# Connecting to roster database

ctab = sqlite3.connect("roster.db")

#ctab.execute("DROP TABLE ROSTER_LIST")

# Creating table for database. PLEASE NOTE: if the table has already been created # out the statement

#ctab.execute("CREATE TABLE ROSTER_LIST(NAME TEXT, SPECIES TEXT, IQ INTEGER);")

# Inserting data into table

ctab.executemany("INSERT INTO ROSTER_LIST Values(?,?,?)", rosterValues)

#Save the changes

ctab.commit()

#Update species of Korben Dallas to be Human

ctab.execute("UPDATE ROSTER_LIST set SPECIES = 'Human' where SPECIES = 'Meat Popsicle'")

#Save the changes

ctab.commit()

#Display the names and IQs of everyone in the table who is classified as Human

ctab_grab = "SELECT * FROM ROSTER_LIST  WHERE SPECIES = 'Human'"

cursor = ctab.execute(ctab_grab)

rows = cursor.fetchall()

print rows
