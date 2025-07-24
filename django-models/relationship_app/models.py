# relationship_app/models.py
from django.db import models
from django.contrib.auth.models import User

# --- Keep your existing models: Author, Library, Librarian, UserProfile ---
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book', related_name='libraries')
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    USER_ROLE_CHOICES = (('Admin', 'Admin'), ('Librarian', 'Librarian'), ('Member', 'Member'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default='Member')
    def __str__(self):
        return f'{self.user.username} - {self.role}'


# --- Update the Book model below ---

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        # Define custom permissions for the Book model
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title