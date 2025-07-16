from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Book model.
    """
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for these fields in the admin sidebar
    list_filter = ('author', 'publication_year')
    
    # Add a search bar to search by these fields
    search_fields = ('title', 'author')

