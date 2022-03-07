from ast import Pass
from django.contrib import admin
from .models import Books
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display=['name','price','author','publisher']

admin.site.register(Books,BooksAdmin)