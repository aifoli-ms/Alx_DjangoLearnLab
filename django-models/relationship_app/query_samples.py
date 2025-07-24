# relationship_app/query_samples.py
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

print("--- Running Sample Queries ---")

# 1. Query all books by a specific author (George Orwell)
print("\n[Query 1: Books by George Orwell]")
try:
    author_orwell = Author.objects.get(name='George Orwell')
    orwell_books = Book.objects.filter(author=author_orwell)
    for book in orwell_books:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print("Author 'George Orwell' not found.")

# 2. List all books in a specific library (Central City Library)
print("\n[Query 2: Books in Central City Library]")
try:
    city_library = Library.objects.get(name='Central City Library')
    # Access books through the ManyToMany relationship
    library_books = city_library.books.all()
    for book in library_books:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print("Library 'Central City Library' not found.")


# 3. Retrieve the librarian for a library (Central City Library)
print("\n[Query 3: Librarian for Central City Library]")
try:
    city_library = Library.objects.get(name='Central City Library')
    # Access the librarian through the OneToOne relationship
    # We use the related_name 'librarian' defined in the Library model
    print(f"- The librarian is {city_library.librarian.name}")
except Library.DoesNotExist:
    print("Library 'Central City Library' not found.")
except Librarian.DoesNotExist:
    print("Librarian for this library not found.")

print("\n--- Queries Finished ---")