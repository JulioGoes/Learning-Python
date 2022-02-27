import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mydatabase"
)

mycursor = mydb.cursor()

'''
    CREATE DATABASE
'''
# Criando um banco de dados
# mycursor.execute('CREATE DATABASE mydatabase')

'''
    CREATE TABLE
'''
# Criando uma tabela no banco de dados
# mycursor.execute("CREATE TABLE customers (\
#     id INT AUTO_INCREMENT PRIMARY KEY,\
#     name VARCHAR(255),\
#     address VARCHAR(255))")

'''
    INSERT INTO (TAG: PREVENT SQL INJECTION)
'''
# Inserindo dados no banco de dados
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# Inserindo muitos dados no banco de dados
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)

# Commitando as inserções
# mydb.commit()

# Mostrando as últimas adições no terminal
# print(mycursor.rowcount, "was inserted.")


'''
    UPDATE + SET + WHERE (TAG: PREVENT SQL INJECTION)
'''
# sql = "UPDATE customers SET address =\
#       'Canyon 123' WHERE address = 'Valley 345'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")


'''
    DROP TABLE
'''
# Deletando uma tabela
# sql = "DROP TABLE customers"
# mycursor.execute(sql)

# Deletando uma tabela apenas se ela existe
# sql = "DROP TABLE IF EXIST customers"
# mycursor.execute(sql)


'''
    SHOW TABLES
'''
# Mostrando as tabelas do banco de dados
# mycursor.execute('SHOW TABLES')

# for x in mycursor:
#     print(x)


"""
    SELECT
"""
# mycursor.execute('SELECT name, address FROM customers')
# myresult = mycursor.fetchone()
# print(myresult)

# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)


'''
    SELECT + WHERE
'''
# sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for i in myresult:
#     print(i)


'''
    SELECT + LIKE
'''
# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for i in myresult:
#     print(i)


'''
    SELECT + LIMIT
'''
# mycursor.execute('SELECT * FROM customers LIMIT 5')
# myresult = mycursor.fetchall()

# for i in myresult:
#     print(i)


'''
    SELECT + LIMIT + OFFSET
'''
# mycursor.execute('SELECT * FROM customers LIMIT 5 OFFSET 2')
# myresult = mycursor.fetchall()

# for i in myresult:
#     print(i)


'''
    PREVENT SQL INJECTION
'''
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()

# for i in myresult:
#     print(i)


'''
    ORDER BY
'''
# sql = "SELECT * FROM customers ORDER BY name"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for i in myresult:
#     print(i)


'''
    ORDER BY DESC
'''
# sql = "SELECT * FROM customers ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for i in myresult:
#     print(i)


'''
    DELETE
'''
# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")


'''
    DELETE + WHERE
'''
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")


"""
    INNER JOIN
"""
# sql = "SELECT \
#     users.name AS user, \
#     products.name AS favorite \
#     FROM users \
#     INNER JOIN products ON users.fav = products.id"

# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for i in myresult:
#     print(i)


"""
    SELECT + INNER JOIN
"""
# sql = "SELECT \
#     users.name AS user, \
#     products.name AS favorite \
#     FROM users \
#     INNER JOIN products ON users.fav = products.id"

# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for i in myresult:
#     print(i)
