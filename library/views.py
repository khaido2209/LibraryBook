from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpResponse
from .models import Category, Book, Borrower, BorrowBook, Author
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    bookitem = Book.objects.all()
    cateitem = Category.objects.all()

    paginator = Paginator(bookitem,3)
    page_Number = request.GET.get('page',1)
    try:
        bookpage = paginator.page(page_Number)
    except PageNotAnInteger:
        bookpage = paginator.page(1)
    except EmptyPage:
        bookpage = paginator.page(paginator.num_pages)

    context ={
        'book' : bookitem,
        'category' : cateitem,
        'paging' : bookpage,
        'cateview':cate_view,
    }
    return render(request, "library/index.html",context)


def cate_view(request, category_id):
    cate_view= Category.objects.get(pk = category_id)
    cateitem = Category.objects.all()
    bookitem2 = Book.objects.all()

    paginator = Paginator(bookitem2, 3)
    page_Number = request.GET.get('page', 1)
    try:
        bookpage2 = paginator.page(page_Number)
    except PageNotAnInteger:
        bookpage2 = paginator.page(1)
    except EmptyPage:
        bookpage2 = paginator.page(paginator.num_pages)

    context1={
        'cate':cate_view,
        'catename': cateitem,
        'paging2': bookpage2,
    }
    return render(request, "library/cateview.html", context1)

from django.views import generic

class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book