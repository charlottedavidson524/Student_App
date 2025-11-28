import sqlite3

class Database:
    """
    Create database layer.
    """
    def __init__(self, db_name: str = "library.db"):
        """
        Initialise a database.

        Args:
            db_name (str): Name of database.
        """
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """
        Create a SQL table.
        """
        query = """
        CREATE TABLE IF NOT EXISTS library (
            id INTEGER PRIMARY KEY AUTOIMPLEMENT
            author TEXT NOT NULL
            title TEXT NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_book(self, author: str, title: str):
        """
        Create book data.

        Args:
            author (str): Author's name.
            title (str): Book title.
        """
        query = "INSERT INTO library (author, title) VALUES (?, ?)"
        self.conn.execute(query, (author, title))
        self.conn.commit()

    def fetch_book(self):
        """
        Pull back all library records/list of books.
        """
        query = "SELECT * FROM library"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def delete_book(self, book_id):
        """
        Delete record of a book.
        """
        self.conn.execute("DELETE FROM contacts WHERE id= ?", (book_id,))
        self.conn.commit()

