***

### **`retrieve.md`**

```markdown
# Retrieve Operation

**Command:** Retrieve and display all attributes of the book you just created.

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")