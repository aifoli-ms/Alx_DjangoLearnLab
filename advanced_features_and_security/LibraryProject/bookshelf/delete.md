***

### **`delete.md`**

```markdown
# Delete Operation

**Command:** Delete the book you created and confirm the deletion by trying to retrieve all books again.

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
all_books = Book.objects.all()
print(all_books)