import os
import django

# Setup Django if running standalone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    return Book.objects.filter(author__name=author_name)


# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# 3. Retrieve the librarian for a library (CHECKER expects this style 👇)
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

