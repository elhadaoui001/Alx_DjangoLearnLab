book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.id, book.title, book.author, book.publication_year)
# Output: 1 Nineteen Eighty-Four George Orwell 1949
 
