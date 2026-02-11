import sqlite3

db = sqlite3.connect("pushups.db")
cursor = db.cursor()

if True:
    cursor.execute("""CREATE TABLE pushups (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        set_number INTEGER NOT NULL,	
        reps INTEGER NOT NULL
    );""")


# example
# pushups_list = [11, 12, 8, 11, 7, 5]
# date = "'2024-02-02'"
# max_id = cursor.execute("SELECT MAX(id) from pushups").fetchone()[0]
#
# db_id = max_id + 1
# for i in range(0, len(pushups_list)):
#     cursor.execute(f"INSERT INTO pushups VALUES ({db_id}, {date}, {i + 1}, {pushups_list[i]})")
#     db_id += 1
#
# cursor.execute("DELETE FROM pushups WHERE date in ('2024/02/02')")
# cursor.execute("UPDATE pushups SET date = '2024-02-01' WHERE date in ('2024/02/01')")
#
# db.commit()

cursor.close()
