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
    
    added_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        help_text="User who added this book"
    )

    class Meta:
        # Ensures that you cannot have two books with the same title and author
        unique_together = [['title', 'author']]
        # Sets the default ordering for querysets
        ordering = ['title']

    def __str__(self):
        """
        Returns a string representation of the book, which is its title.
        """
        return self.title