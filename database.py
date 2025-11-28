import sqlite3

class Database:
    """
    Create database layer.
    """
    def __init__(self, db_name = "library.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """
        """
        pass

    def insert_book(self):
        """
        """
        pass

    def fetch_book(self):
        """
        """
        pass

    def delete_book(self):
        """
        """
        pass

