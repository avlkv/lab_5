from django.shortcuts import render
from django.views.generic import View, ListView
from lab5.models import Book, Review


# Список книг
class ListbookView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    paginate_by = 3

    def get(self, request, page=1):

        books = Book.objects.all()

        return render(request, 'book_list.html', {"books": books})

# Страница с информацией о книге и отзывами
class bookView(View):

    def get(self, request, book_id):

        book = Book.objects.get(id=book_id)
        reviews = Review.objects.filter(book_id=book_id)

        return render(request, 'book.html', {"book": book, "reviews": reviews})
