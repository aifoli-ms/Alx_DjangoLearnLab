# relationship_app/urls.py
from django.urls import path
from . import views

app_name = 'relationship_app' # This is important for namespacing

urlpatterns = [
    # Previous URLs
    path('books/', views.list_books, name='book-list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),

    # New Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]