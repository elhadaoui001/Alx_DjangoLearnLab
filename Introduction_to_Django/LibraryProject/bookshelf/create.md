# Create Operation

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected output: a new Book object is created
print(book.id, book.title, book.author, book.publication_year)
# Example output: 1 1984 George Orwell 1949
 
