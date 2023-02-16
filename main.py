# Primero de importa la data base sqlite3
import sqlite3
# Luego se conecta la data base creada con sqlite
db_connection = sqlite3.connect('tablaDouglas1.db')
# luego se tiene que crear un crusor, y a traves de este cursor se tiene que agregar los valores de la tabla
db_cursor = db_connection.cursor()

# con la variable donde esta el cursor y .execute se crea la tabla y se agregan los valores

# db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Alumnos VALUES(1,'Martina', 'Ramos')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'Joseida', 'Arismndi')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'Rafael', 'Ramos')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'Dogly', 'Guzman')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'Francisca', 'Orence')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'Argentina', 'Campeon')")
db_cursor.execute("INSERT INTO Alumnos VALUES(7,'Segundo', 'Francia')")
db_cursor.execute("INSERT INTO Alumnos VALUES(8,'Odalys', 'Estaba')")
db_cursor.execute("INSERT INTO Alumnos VALUES(9,'Douglas', 'Guzmán')")
db_cursor.execute("INSERT INTO Alumnos VALUES(10,'Manuela', 'Martinez')")

db_connection.commit()

db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Martina'")

filas = db_cursor.fetchall()

print(filas)

db_connection.close()