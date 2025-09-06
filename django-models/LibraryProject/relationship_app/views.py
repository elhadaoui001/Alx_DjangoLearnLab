from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library, Librarian

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    output = ""
    for book in books:
        output += f"{book.title} by {book.author.name}\n"
    return HttpResponse(output, content_type="text/plain")
    
    # class-based view: list all books
class LibraryDetailView(DetailView):
    model = Library

    def render_to_response(self, context, **response_kwargs):
        library = context["library"]
        output = f"Library: {library.name}\nBooks:\n"
        for book in library.books.all():
            output += f"- {book.title} by {book.author.name}\n"
        return HttpResponse(output, content_type="text/plain")


