import sqlite3

db = sqlite3.connect("pushups2.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE pushups (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    set_number INTEGER NOT NULL,	
    reps INTEGER NOT NULL);
    """)

cursor.close()
