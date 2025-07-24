from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Book model.
    """
    # Display these fields in the admin list view
    list_display = ('title', 'author', 'publication_year', 'added_by')
    
    # Add filters for these fields in the admin sidebar
    list_filter = ('author', 'publication_year', 'added_by')
    
    # Add a search bar to search by these fields
    search_fields = ('title', 'author')
    
    # Automatically set the added_by field to the current user when saving
    def save_model(self, request, obj, form, change):
        if not change:  # Only set on creation, not on update
            obj.added_by = request.user
        super().save_model(request, obj, form, change)

