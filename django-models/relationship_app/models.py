# relationship_app/models.py
from django.db import models
from django.contrib.auth.models import User

# --- Keep your existing models: Author, Book, Library, Librarian ---
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
    def __str__(self):
        return self.name

# --- Add the new UserProfile model below ---

class UserProfile(models.Model):
    """
    Extends the default User model to include a role.
    """
    USER_ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    # Link to the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # Role field with predefined choices and a default
    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default='Member')

    def __str__(self):
        return f'{self.user.username} - {self.role}'