import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM agenda"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)