from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Book(models.Model):
    """
    Represents a book with a title, author, and publication year.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    # Example of how to reference the custom user model
    added_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        help_text="User who added this book"
    )

    def __str__(self):
        """
        Returns a string representation of the book, which is its title.
        """
        return self.title

