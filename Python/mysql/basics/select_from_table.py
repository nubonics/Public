import mysql.connector


mydb = mysql.connector.connect(
		host = 'localhost',
		user = 'root',
		passwd = 'password',
		database = 'testdb',

)

my_cursor = mydb.cursor()
#print(my_cursor)

# Select everything from the 'users' table
my_cursor.execute("SELECT * FROM users")

# Obtain the information and save the information to a variable
result = my_cursor.fetchall()
# The table consists of columns 'name, email, age, unique_id'

print()
for row in result:
	name       = row[0]
	email      = row[1]
	age        = row[2]
	unique_key = row[3]

	print(name + "%s" %email + " %s" %age + " %s" %unique_key)
