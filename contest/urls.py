from unicodedata import name
from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('student',views.student,name='student'),
    path('teacher',views.teacher,name='teacher'),
    path('bank_list',views.bank_list,name='bank_list'),
    path('add_bank',views.add_bank,name='add_bank'),

    path('question_list/<int:question_bank_id>/',views.question_list,name='question_list'),
    path('question_add/<int:question_bank_id>/',views.question_add,name='question_add'),
    path('question_add_batch/<int:question_bank_id>/',views.question_add_batch,name='question_add_batch'),

    path('contest_manage',views.contest_manage,name='contest_manage'),
    path('contest_create',views.contest_create,name='contest_create'),
    path('contest_config/<int:contest_id>/',views.contest_config,name='contest_config'),
    path('contest/<int:contest_id>/',views.contest,name='contest')
    
]