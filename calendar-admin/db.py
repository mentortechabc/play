import sqlite3
from sqlite3.dbapi2 import Connection


def create_connection(path_to_db=":memory:") -> Connection:
    """
    Creates a connection to the database path.
    By default returns a connection to memory.
    """
    return sqlite3.connect(path_to_db)


def create_admininfo_table(connection: Connection) -> None:
    """
    Creates AdminInfo(id, email, password) table using specified connection.
    """

    connection.execute("""
        CREATE TABLE IF NOT EXISTS AdminInfo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL UNIQUE
    );
    """)

    connection.commit()
