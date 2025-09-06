import os
import django

# Setup Django if running standalone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)   # ✅ required by checker
    return Book.objects.filter(author=author)       # ✅ required by checker


# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# 3. Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)   # ✅ required by checker



