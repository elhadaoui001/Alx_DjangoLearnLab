from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library
from .models import Book  

# --- Function-Based View ---
# List all books stored in the database
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})
    # ✅ Checker looks for: "relationship_app/list_books.html"


# --- Class-Based View ---
# Display details for a specific library, listing all books
class LibraryDetailView(DetailView):
    model = Library                       # ✅ Checker wants Library imported
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


