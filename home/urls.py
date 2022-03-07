from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add',views.addBook,name='addBook'),
    path('list',views.bookList,name='bookList'),
    path('delBook/<int:id>',views.delBook,name='delBook'),
    path('edit',views.editBook,name='editBook'),
    path('updateBook',views.updateBook,name='updateBook'),

    path('test',views.test,name='test'),
    path('base',views.base,name='base')
]