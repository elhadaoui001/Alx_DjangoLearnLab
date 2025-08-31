books = Book.objects.all()
for book in books:
    print(book.id, book.title, book.author, book.publication_year)
# Output: 1 1984 George Orwell 1949
 
