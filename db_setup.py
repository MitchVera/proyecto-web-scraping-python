import sqlite3

def create_db():
    # Conectar a la base de datos (se crea si no existe)
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    # Crear las tablas necesarias
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS scraped_data (
        id INTEGER PRIMARY KEY,
        url TEXT,
        title TEXT,
        description TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS processed_text (
        id INTEGER PRIMARY KEY,
        text TEXT,
        summary TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS combined_results (
        id INTEGER PRIMARY KEY,
        url TEXT,
        title TEXT,
        description TEXT,
        summary TEXT
    )
    ''')

    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

# Llamar a la función para crear la base de datos y las tablas
if __name__ == '__main__':
    create_db()