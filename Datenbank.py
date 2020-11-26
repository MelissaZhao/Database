## Connecting to the database
## importing 'mysql.connector' as mysql for convenient

import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db= mysql.connect(
    host="localhost",
    user="root",
    password="3Niandaojishi",
    database="MelissaZY"
)


## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor=db.cursor()

## create 2 tables 'account' and 'users'
## then use 'DROP TABLE table_name' statement to drop existed table 'users' from a database
cursor.execute("DROP TABLE peers ")

## creating the 'user' table with the 'PRIMARY KEY'
cursor.execute("CREATE TABLE buddies (id int(11) NOT NULL AUTO_INCREMENT,first_name VARCHAR(255), family_name VARCHAR(255),PRIMARY KEY(id))")

## defining the Query1
query1 = "INSERT INTO buddies (first_name, family_name) VALUES (%s, %s)"
## storing values in a variable
values = [
    ("Peter", "B"),
    ("Maria", "I"),
    ("Michael", "J"),
    ("Kaho", "N"),
    ("Teressa", "R"),
    ("Steffen", "K")
]

## executing the query with values
cursor.executemany(query1, values)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

## defining the Query2
query2 = "SELECT * FROM buddies WHERE id=5"

## getting records from the table
cursor.execute(query2)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)

## defining the Query3
query3 = "SELECT * FROM buddies ORDER BY family_name DESC"

## getting records from the table
cursor.execute(query3)

## fetching all records from the 'cursor' object
names = cursor.fetchall()

## Showing the data
for name in names:
    print(name)

## getting all the tables which are present in 'MelissaZY' database
cursor.execute("SHOW TABLES")

## fetching all databases from the 'cursor' object
databases = cursor.fetchall()
for database in databases:
    print(database)