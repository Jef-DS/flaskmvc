import sqlite3
from flask import g, current_app

def get_connection() ->sqlite3.Connection:
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(current_app.config['DATABASE_URI'])
    return db

def init_db():
    with get_connection() as conn, current_app.open_resource('init_db.sql', mode='r') as sqlfile:
        script = sqlfile.read()
        conn.executescript(script)
        conn.commit()

def get_klanten():
    with get_connection() as conn:
        cursor = conn.cursor()
        resultaat = cursor.execute("SELECT nr, naam FROM klant")
        return resultaat.fetchall()

def insert_klant(nr:int, naam:str) -> int:
    with get_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO klant (nr, naam) VALUES (?, ?)", (nr, naam))
            conn.commit()
            return cursor.rowcount
        except sqlite3.IntegrityError as e:
            raise ValueError(e.args)