import mysql.connector


mydb = mysql.connector.connect(
		host = 'localhost',
		user = 'root',
		passwd = 'password',
		database = 'testdb',
		table = 'users', # the name of the table, this is needed ONLY if the table has already been created.

)

my_cursor = mydb.cursor()
#print(my_cursor)

# Create Example Table
my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(4), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

"""
VARCHAR is a variable of characters with a limit.
- in this example, the column 'name', has a maximum of 255 characters, represented as hexadecimal
-- we cannot exceed 255 characters at any time.

INTEGER
- in this example, the column 'age', has a maximum of 4 integers, this is because "no one" is older than 9,999 years old. 
-- the comma in 9,999 is just for human reference / understanding, it is not included as a character, so INTEGER(4) still remains true
--- i do not know the limit of INTEGER at this time, I am assuming it is the same as VARCHAR's limit of 255

AUTO_INCREMENT
- this is a counter in a loop ( looking at this command, as we would view python code )

PRIMARY KEY
- this is a unique "key", like a key is an a python dictionary, which is a unique identifier.
-- there are NO PRIMARY KEY duplicates
--- the purpose of the PRIMARY KEY is to distinguish between columns that may contain the same data, such-as the same email address
---- using a PRIMARY KEY, this allows us to distinguish between the two 'records' or entries into the database, as separete entities.
"""

my_cursor.execute("SHOW TABLES")

print()
for table in my_cursor:
	table = table[0]
	print(table)
