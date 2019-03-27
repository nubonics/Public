import mysql.connector


mydb = mysql.connector.connect(
		host = 'localhost',
		user = 'root',
		passwd = 'password',

)

my_cursor = mydb.cursor()
#print(my_cursor)

# Create a database named testdb
#my_cursor.execute('CREATE DATABASE testdb')

my_cursor.execute("SHOW DATABASES")

print()
for database in my_cursor:
	database = database[0]
	print(database)
