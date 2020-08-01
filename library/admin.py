from django.contrib import admin
from django.urls import reverse
from .models import Category, Book, Borrower, BorrowBook, Author

class BorrowedBookInLines (admin.TabularInline):
    model = BorrowBook

@admin.register(Book)
class BookAdmin (admin.ModelAdmin):
    list_display = ('name_book', 'description', 'get_cates', 'get_authors', 'quantity_book', 'get_status', 'image_preview')
    # fields = ['name_book', 'status', 'cate', 'quantity_book', 'author']
    ordering = ['name_book']
    list_filter = ('cate', 'author')
    #inlines = [BorrowBookInline]
    fieldsets = (
        ('Information', {
            'fields': ('name_book', 'description', ('cate', 'author'), 'image')
        }),
        ('Availability', {
            'fields': [('quantity_book',)]
        }),
    )

    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True


@admin.register(BorrowBook)
class BorrowBookAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'book', 'borrow_date', 'due_back', 'set_statuss','status')
    fields = [('borrower', 'book'),'borrow_date' , 'due_back','status']
    ordering = ['due_back']
    list_filter = ['due_back']

    def __get_absolute_url__(self):
        return reverse('book-detail', args=[str(self.id)])

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_cate']
    fields = ['name_cate']

@admin.register(Borrower)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'cmnd']
    fields = ['name', 'phone', 'cmnd']
    inlines = [BorrowedBookInLines]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name_author']
    fields = ['name_author']


