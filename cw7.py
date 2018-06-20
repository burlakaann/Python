#1
import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS bookss(id integer primaty key, title text, author text)''')

cursor.execute("INSERT INTO bookss VALUES (1, 'The Martian', 'Andy Weir')")
cursor.execute("INSERT INTO bookss VALUES (2, 'The Hunger Games', 'Suzanne Collins')")
cursor.execute("INSERT INTO bookss VALUES (3, 'The Windup Girl ', 'Paolo Bacigalupi ')")
cursor.execute("INSERT INTO bookss VALUES (4, 'Cloud Atlas ', 'David Mitchell ')")
cursor.execute("INSERT INTO bookss VALUES (5, 'Spin', 'Robert Charles Wilson ')")

for _, title, author in cursor.execute('select * from bookss'):
	print (author, title)

connection.commit()
connection.close()
