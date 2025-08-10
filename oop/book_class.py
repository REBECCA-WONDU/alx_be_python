class Book:
    """
    A class to represent a book with title, author, and publication year.
    Implements several magic methods for better object representation.
    """

    def __init__(self, title, author, year):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Return a user-friendly string representation of the book.
        
        Returns:
            str: String in format "Title by Author, published in Year"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Return an official string representation that can recreate the object.
        
        Returns:
            str: String in format "Book('Title', 'Author', Year)"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"