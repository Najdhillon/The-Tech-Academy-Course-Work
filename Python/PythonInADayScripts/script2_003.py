import sqlite3

# Connect to database 'simpson.db'

conn = sqlite3.connect('simpson.db')

#conn.execute("CREATE TABLE SIMPSON_INFO (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, GENDER TEXT, AGE INT, OCCUPATION TEXT);")


# Add Bart Simpson to table

conn.execute("Insert into SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION) VALUES ('Bart Simpson', 'Male', 10, 'Student')");

# Add Homer Simpson to table

conn.execute("Insert into SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION) VALUES ('Homer Simpson', 'Male', 40, 'Nuclear Plant')");

# Add Bart Simpson to table

conn.execute("Insert into SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION) VALUES ('Lisa Simpson', 'Female', 8, 'Student')");


# Save changes

conn.commit()


# Print number of changes to database
changes=conn.total_changes
print"Number of changes:", changes
