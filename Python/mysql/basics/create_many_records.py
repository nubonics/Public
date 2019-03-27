import mysql.connector


mydb = mysql.connector.connect(
		host = 'localhost',
		user = 'root',
		passwd = 'password',
		database = 'testdb',

)

my_cursor = mydb.cursor()
#print(my_cursor)

# Initialize the placeholder
sql_command = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"

# Populate the placeholder
many_records = [("John", "john@codemy.com", 40),
				("Tim", "tim@tim.com", 32),
				("Mary", "Mary@mary.com", 21),
				("Steve", "steve@steveEmail.com", 57),
				("Tina", "tina@somethingelse.com", 29),
]

# Execute the command, and add the record to the table
my_cursor.executemany(sql_command, many_records)
mydb.commit()
