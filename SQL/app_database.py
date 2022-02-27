import sqlite3
from contextlib import closing

with closing(sqlite3.connect("bancodedados/aquarium.db")) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()
        print(rows)

# Criando a conexão com o banco de dados
connection = sqlite3.connect('bancodedados/aquarium.db')

# Criando o cursor, possibilitando a adição de comandos SQL
cursor = connection.cursor()

# Criando uma tabela e definindo suas colunas
cursor.execute('CREATE TABLE IF NOT EXISTS fish \
               (name text, species text, tank_number integer)')

# Inserindo valores na tabela
cursor.execute("INSERT INTO fish VALUES ('Sammy', 'Shark', 1)")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'Cuttlefish', 7)")

# Imprime na tela somente onde o nome do peixe for 'Jaime
target_fish_name = "Jamie"
rows = cursor.execute(
    "SELECT name, species, tank_number FROM fish WHERE name = ?",
    (target_fish_name,),
).fetchall()
print(rows)

# Alterando o peixe 'Sammy' de Tank, ou seja, alterando
# valores no banco de dados
new_tank_number = 2
moved_fish_name = 'Sammy'
cursor.execute(
    "UPDATE fish SET tank_number = ? WHERE name = ?",
    (new_tank_number, moved_fish_name)
)

# Imprime na tela todas as linhas da tabela 'fish'
rows = cursor.execute("SELECT name, species, \
                      tank_number FROM fish").fetchall()
print(rows)

# Libertando Sammy do Aquário, ou seja, removendo valores do banco de dados
released_fish_name = 'Sammy'
cursor.execute(
    "DELETE FROM fish WHERE name = ?",
    (released_fish_name,)
)

# Imprime na tela todas as linhas da tabela 'fish'
rows = cursor.execute("SELECT name, species, \
                      tank_number FROM fish").fetchall()
print(rows)

connection.commit()
connection.close()
