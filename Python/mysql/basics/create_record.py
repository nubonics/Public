import mysql.connector


mydb = mysql.connector.connect(
		host = 'localhost',
		user = 'root',
		passwd = 'password',
		database = 'testdb',
		table = 'users', 

)

my_cursor = mydb.cursor()
#print(my_cursor)

# Initialize the placeholder
sql_command = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"

# Populate the placeholder
single_record = ("John", "john@codemy.com", 40)

# Execute the command, and add the record to the table
my_cursor.execute(sql_command, single_record)
