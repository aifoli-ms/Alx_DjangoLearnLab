# relationship_app/views.py

# --- Update imports ---
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Book, Library, UserProfile, Author
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.urls import reverse_lazy
from django.forms import ModelForm


# --- Keep all your existing views and role-checking functions ---
# (list_books, LibraryDetailView, register_view, login_view, logout_view, admin_view, etc.)


# --- Add a simple form for the Book model ---
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']


# --- Add New Permission-Protected Views ---

@permission_required('relationship_app.can_add_book', login_url='/login/')
def book_create(request):
    """View to add a new book, protected by permission."""
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:book-list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_change_book', login_url='/login/')
def book_update(request, pk):
    """View to edit an existing book, protected by permission."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:book-list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_delete_book', login_url='/login/')
def book_delete(request, pk):
    """View to delete a book, protected by permission."""
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('relationship_app:book-list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'object': book})