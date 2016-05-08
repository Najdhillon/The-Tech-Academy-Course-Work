import sqlite3

conn = sqlite3.connect('simpson.db')

# get data from database

#cursor = conn.execute("Select * from SIMPSON_INFO")

#cursor = conn.execute("SELECT * FROM SIMPSON_INFO where name = 'Homer Simpson'")

#cursor = conn.execute("SELECT * FROM SIMPSON_INFO where gender = 'Female'")

#cursor = conn.execute("SELECT * FROM SIMPSON_INFO where Occupation = 'Student'")

cursor = conn.execute("UPDATE SIMPSON_INFO set AGE=41 where NAME='Homer Simpson'")

#Save changes

conn.commit()

#Print number of changes

changes = conn.total_changes

print "Number of changes:",changes

#Get Data from database

cursor = conn.execute("Select * from SIMPSON_INFO")

#print cursor

rows = cursor.fetchall()

print rows


#DONT RUN THIS CODE:
#conn.execute("DROP TABLE SIMPSON_INFO")




