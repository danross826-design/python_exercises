import mysql.connector

mydb = mysql.connector.connect(
	host => 'localhost',
	user => 'root',
	password => '1234',
	database => 'db'
	)

cursor = mydb.cursor()

query = "SELECT * FROM users where first_name like s%"

data = cursor.execute(query)

print(data)

mydb.close()

