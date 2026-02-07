def init_db(db):
    db.execute("""
    CREATE TABLE IF NOT EXISTS doctors(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               category_id INTEGER,
               experience REAL,
               rating REAL
               )
    """)

    db.execute("""
    CREATE TABLE IF NOT EXISTS categories(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT
               )
    """)

    db.execute("""
    CREATE TABLE IF NOT EXISTS symptoms(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               weight INTEGER
               )
    """)

    db.execute("""
    CREATE TABLE IF NOT EXISTS mapping(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               symptom_id INTEGER,
               category_id INTEGER
               )
    """)