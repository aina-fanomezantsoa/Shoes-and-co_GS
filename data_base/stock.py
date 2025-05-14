import sqlite3
import os

def creat_bd():
    conn =None
    try:
        db_path = os.path.join('data_base', 'stock.sqlite3')
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("""
                CREATE TABLE IF NOT EXISTS Produits (reference INTEGER PRIMMARY KEY, description TEXT, qt INTEGER, prix_achat INTEGER, prix_vente INTEGER)
        """)
        conn.commit()
        return conn
    except sqlite3.Error as e:
        print(f"Erreur SQLite: {e}")
        return None

