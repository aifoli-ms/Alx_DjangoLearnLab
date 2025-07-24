# relationship_app/views.py

# --- Keep existing imports ---
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import DetailView
from .models import Book, Library, UserProfile # Add UserProfile import

# --- Add this new import ---
from django.contrib.auth.decorators import user_passes_test


# --- Keep existing views: list_books, LibraryDetailView, register_view, login_view, logout_view ---
# (No changes needed for the existing views)


# --- Add Role-Checking Functions ---
# These functions will be used by the decorator to verify a user's role.

def is_admin(user):
    """Checks if the user has the 'Admin' role."""
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Admin'

def is_librarian(user):
    """Checks if the user has the 'Librarian' role."""
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Librarian'

def is_member(user):
    """Checks if the user has the 'Member' role."""
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Member'


# --- Add New Role-Based Views ---

@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    """View accessible only by users with the 'Admin' role."""
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    """View accessible only by users with the 'Librarian' role."""
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    """View accessible only by users with the 'Member' role."""
    return render(request, 'relationship_app/member_view.html')