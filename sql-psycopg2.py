import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# builds a cursor object of the database
cursor = connection.cursor()

# Query #1 -select all records from the "artist" table
cursor.execute('SELECT * FROM "artist"')

# fetch the results(mulyiple)
results = cursor.fetchall()

# fetch the results(single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(results)