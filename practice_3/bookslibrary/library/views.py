# Create your views here.

from library.models import Book
from library.models import Author
from library.models import Publisher
from django.shortcuts import render


def books(request, sub):
    d = {'books': Book.objects.all()}
    return render(request, 'books.html', d)


def book(request, sub):
    book = Book.objects.get(id=sub)
    d = {'book': book, 'authors': book.authors.all()}
    return render(request, 'book.html', d)


def authors(request):
    d = {'authors': Author.objects.all()}
    return render(request, 'authors.html', d)


def author(request, sub):
    d = {'author': Author.objects.get(id=sub)}
    return render(request, 'author.html', d)
