class Book:
    def __init__(self, author: str, title: str):
        """
        Initialise a new book instance.

        Args:
            author (str): The name of the book's author.
            title (str): The title of the book.
        """
        self.author = author
        self.title = title

    def __str__(self):
        """
        Return a human readable string representation of the book.

        Returns:
            str: A string in the format "author - title".
        """
        return f"{self.author} - {self.title}"
