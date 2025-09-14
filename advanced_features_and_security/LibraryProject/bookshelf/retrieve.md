# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve all books
Book.objects.all()
# <QuerySet [<Book: 1984>]>

# Retrieve a specific book by title
b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year
# ('1984', 'George Orwell', 1949)


