import sqlite3

def create_db():
    conn = sqlite3.connect('amity.db')

    instructions = None

    with open('amity.sql') as sql:
        instructions = sql.read()

    c = conn.cursor()
    c.execute(instructions)
    c.commit()
    c.close()

if __name__ == "main":
    create_db()