import psycopg2

class DatabaseWriter(object):
    def __init__():
        pass

    def connect():
        """Connect to the PostgreSQL database.  Returns a database connection."""
        try:
            return psycopg2.connect("dbname=amity_manager")
        except:  # while normally using except without specifying an exception is bad practice, I believe it is acceptable in this narrow case.
            print("Connection failed")

    def insert_in_table(table_name, data):
        pass

    def update_table(table_name, data):
        pass

    def delete_from_table(table_name, *data):
        db = connect()
        c = db.cursor()
        if args:
            c.execute("""DELETE FROM %s VALUES (%s)""", (table, data,))
            #I don't think this will work with most inputs right now. Not user friendly :)
        else:
            c.execute("""DELETE FROM %s""", (table_name,))
        db.commit()
        db.close()

    # def select_from_database():