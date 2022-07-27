import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'adamtaieb'
PASSWORD = 'cluster'
DATABASE = 'Hollywood'

try:
    connection = psycopg2.connect(host=HOSTNAME, user= HOSTNAME, password=PASSWORD, dbname=DATABASE)
except:
    print('connection failed')


cursor = connection.cursor()

query = "SELECT * FROM actors"

cursor.execute(query)

results = cursor.fetchall()

connection.close()

print(cursor)