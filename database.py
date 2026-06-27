import sqlite3

def init_db():
    conn = sqlite3.connect('shg.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS meetings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        transcription TEXT,
        minutes TEXT
    )
    ''')

    conn.commit()
    conn.close()
