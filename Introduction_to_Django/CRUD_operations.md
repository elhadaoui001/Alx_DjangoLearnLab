# CRUD Operations for Book Model

## Create
>>> Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
<Book: 1984>

## Retrieve
>>> Book.objects.all()
<QuerySet [<Book: 1984>]>

## Update
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book.title
'Nineteen Eighty-Four'

## Delete
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
 
