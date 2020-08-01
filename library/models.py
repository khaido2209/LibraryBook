import pymsgbox
from datetime import datetime
import uuid
from django.db import models
from django.urls import reverse
from django.utils import timezone

from django.utils.html import mark_safe
STATUS_CHOICES = (
        ('-', '--------'),
        ('a', 'Đang mượn'),
        ('d', 'Đã trả'),
    )

class Category(models.Model):
    name_cate = models.CharField(max_length=100)

    def __str__(self):
        return self.name_cate


class Author(models.Model):
    name_author = models.CharField(max_length=50)

    def __str__(self):
        return self.name_author


class Book(models.Model):
    #Fields
    status = models.BooleanField(default=1)
    name_book = models.CharField(max_length=100, unique=True)
    quantity_book = models.IntegerField(default=1)
    cate = models.ManyToManyField(Category)
    author = models.ManyToManyField(Author)
    description = models.TextField(null=True,max_length = 1000)
    image = models.ImageField(upload_to='./img', default='./img/default.png')

    def get_status(self):
            if self.quantity_book >= 1:
                return self.status == 1
            else:
                return self.status == 0

    # def check_quantity(self):
    #     if BorrowBook.book == True:
    #         return self.quantity_book - 1
    #     self.quantity_book.save()


    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="50" height="75" />'.format(self.image.url))
        return ""

    def get_authors(self):
        return ",".join([str(p) for p in self.author.all()])

    def get_cates(self):
        return ",".join([str(p) for p in self.cate.all()])

    def __unicode__(self):
        return "{0}".format(self.name_book)

    def __str__(self):
        return self.name_book


class Borrower(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    cmnd = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class BorrowBook(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    book = models.ForeignKey(Book ,on_delete=models.CASCADE)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='-')
    borrow_date = models.DateTimeField(null=True)
    due_back = models.DateTimeField(null=True)

    a= 'Trễ hạn'
    b = 'Chưa tới hạn'

    def set_statuss(self):
        now = timezone.now()
        if self.due_back <= now:
            return self.a
        else:
            return self.b

    def check_available(self):
        if Book.quantity_book != 0:
            return self.book.quantity_book

    def __str__(self):
        return f'{self.id} ({self.book.name_book})'

    def save(self, *args, **kwargs):
        # b = BorrowBook.objects.get(self)
        if (Book.objects.get(id=self.book_id).quantity_book == 0):
            return pymsgbox.alert('Sách Đã Được Mượn Hết!', 'Thông Báo')
        elif(Book.objects.get(id=self.book_id).quantity_book >= 1):
            c = Book.objects.get(id=self.book_id).quantity_book
            c -= 1
            Book.objects.select_related().filter(id=self.book_id).update(quantity_book=c)
        super().save(*args, **kwargs)