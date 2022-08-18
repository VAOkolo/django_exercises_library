from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render


from .models import Book

# Create your views here.
# books = [
#     {'id': 1, 'name': "Harry Potter", "author": "J.K.Rowling"},
#     {'id': 2, 'name': "Lord of the Rings", "author": "Tolkein"},
#     {'id': 3, 'name': "Lirael", "author": "Garth Nix"}
# ]


def not_found_404(request, exception):
    data = { 'err': exception }
    return render(request, '404.html', data)

def server_error_500(request):
    return render(request, '500.html')

def home(request):
    # all_books
    all_books = {'books': Book.objects.all()}
    print(all_books)
    return render(request, 'home.html', all_books)

def show(request, id):
    book = get_object_or_404(Book, pk=id)
    data = {'book': book}
    print(book)
    return render(request, 'show.html', data)
