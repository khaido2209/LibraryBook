from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
from .models import Category, Book, Borrower, BorrowBook, Author

# Create your views here.
def index(request):
    bookitem = Book.objects.all()
    cateitem = Category.objects.all()
    context ={
        'book' : bookitem,
        'category' : cateitem,
    }
    return render(request, "library/index.html", context)