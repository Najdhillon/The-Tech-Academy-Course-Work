import sqlite3
import datetime, time

conn = sqlite3.connect('drilldb.db')
c = conn.cursor()

def create_table():

    c.execute('CREATE TABLE IF NOT EXISTS addStuff(ID INTEGER PRIMARY KEY AUTOINCREMENT, modtime INTEGER)')

def data_entry():
    c.execute("INSERT INTO addStuff VALUES(1,12321)")
    conn.commit()
    c.close()
    conn.close()

def dynamic_data_entry():

    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO addSTUFF (modtime) VALUES (?)", (date))

    conn.commit()

def search_db():

    c.execute("SELECT MAX(modtime) FROM addStuff")
    date = c.fetchall()
    print(date)

    
#create_table()
##data_entry()

#dynamic_data_entry()

search_db()
