import sqlite3
from sqlite3 import Error

# Write a Python script to connect to a SQLite database and create a table.
# Create a program to insert data into a SQLite database using Python.
# Write a Python script to fetch and display data from a SQLite database.
# Create a program to update and delete records in a SQLite database using Python.
# Write a Python script to handle database connection errors.

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    """ create a table from the create_table_sql statement """
    try:
        sql_create_table = """ CREATE TABLE IF NOT EXISTS projects (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    begin_date text,
                                    end_date text
                                ); """
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)

def insert_data(conn, project):
    """ insert a new project into the projects table """
    sql = ''' INSERT INTO projects(name, begin_date, end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def fetch_data(conn):
    """ fetch all rows from the projects table """
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def update_data(conn, project):
    """ update end date of a project """
    sql = ''' UPDATE projects
              SET end_date = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()

def delete_data(conn, id):
    """ delete a project by project id """
    sql = 'DELETE FROM projects WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def main():
    database = "pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create projects table
        create_table(conn)

        # insert data
        project = ('Cool App with SQLite & Python', '2021-01-01', '2021-01-30')
        project_id = insert_data(conn, project)
        project = ('Cool App with SQLite & Python', '2021-01-01', '2021-01-30')
        project_id = insert_data(conn, project)

        # fetch data
        print("Initial data:")
        fetch_data(conn)

        # update data
        update_data(conn, ('2021-02-01', project_id))

        # fetch data
        print("Data after update:")
        fetch_data(conn)

        # delete data
        delete_data(conn, project_id)

        # fetch data
        print("Data after delete:")
        fetch_data(conn)

if __name__ == '__main__':
    main()