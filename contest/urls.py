from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('bank_list',views.bank_list,name='bank_list'),
    path('add_bank',views.add_bank,name='add_bank'),
    path('question_list/<int:question_bank_id>/',views.question_list,name='question_list'),
    path('question_add/<int:question_bank_id>/',views.question_add,name='question_add'),
    path('question_add_batch/<int:question_bank_id>/',views.question_add_batch,name='question_add_batch'),
    
]