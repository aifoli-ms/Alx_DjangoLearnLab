# relationship_app/query_samples.py

import os
import django

# --- CHANGE 1: Point to your project's settings ---
# The original was 'django_models.settings'. It needs to match your project folder.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# --- CHANGE 2: Use a direct import path for the models ---
from relationship_app.models import Author, Book, Library, Librarian

# The rest of the script will now work correctly.

# Clear previous data to avoid duplicates on re-runs
Author.objects.all().delete()
Book.objects.all().delete()
Library.objects.all().delete()
Librarian.objects.all().delete()

# Create some data to work with
author1 = Author.objects.create(name='George Orwell')
author2 = Author.objects.create(name='J.R.R. Tolkien')

book1 = Book.objects.create(title='1984', author=author1)
book2 = Book.objects.create(title='Animal Farm', author=author1)
book3 = Book.objects.create(title='The Hobbit', author=author2)

library1 = Library.objects.create(name='Central Library')
library1.books.add(book1, book2, book3)

librarian1 = Librarian.objects.create(name='Mr. Smith', library=library1)

# --- Queries that will now print output ---

# Query all books by a specific author
orwell_books = Book.objects.filter(author__name='George Orwell')
print(f"Books by George Orwell: {[book.title for book in orwell_books]}")

# List all books in a library
central_library_books = library1.books.all()
print(f"Books in Central Library: {[book.title for book in central_library_books]}")

# Retrieve the librarian for a library
central_librarian = Librarian.objects.get(library__name='Central Library')
print(f"Librarian at Central Library: {central_librarian.name}")