# relationship_app/views.py
from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# 1. Function-Based View to list all books
def list_books(request):
    """
    Queries all books from the database and renders them in a template.
    """
    books = Book.objects.all()  # Fetches all Book objects
    context = {'books': books}
    return render(request, 'list_books.html', context)


# 2. Class-Based View to show details for one library
class LibraryDetailView(DetailView):
    """
    Uses Django's built-in DetailView to display a single library's details.
    """
    model = Library  # Specifies the model this view works with
    template_name = 'library_detail.html'  # Specifies the template to render
    context_object_name = 'library' # Sets the variable name in the template