import sqlite3

# Conectar (o crear) base de datos
conn = sqlite3.connect('datos.db')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS personas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    apellido TEXT,
    color_favorito TEXT,
    alimento_favorito TEXT
)
''')

# Pedir datos al usuario
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
color = input("¿Cuál es tu color favorito?: ")
alimento = input("¿Cuál es tu alimento favorito?: ")

# Insertar en la base de datos
cursor.execute('''
INSERT INTO personas (nombre, apellido, color_favorito, alimento_favorito)
VALUES (?, ?, ?, ?)
''', (nombre, apellido, color, alimento))

# Guardar y cerrar conexión
conn.commit()
conn.close()

print("✅ Datos guardados correctamente en la base de datos.")
