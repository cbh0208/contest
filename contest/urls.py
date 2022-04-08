from django.urls import path
from . import views
urlpatterns=[
    path('bank_list',views.bank_list),
    path('bank/<int:id>/',views.bank),
    path('bank_add',views.bank_add),

    path('question_delete',views.question_delete),
    path('question_add',views.question_add),
    path('question_add_batch',views.question_add_batch),

    path('get_contest_list',views.get_contest_list),
    path('create_contest',views.create_contest),
    path('end_contest',views.end_contest),

    path('get_contest_received',views.get_contest_received)



    # path('',views.index),
    # path('student',views.student,name='student'),
    # path('teacher',views.teacher,name='teacher'),
    # path('bank_list',views.bank_list,name='bank_list'),
    # path('add_bank',views.add_bank,name='add_bank'),

    # path('question_list/<int:question_bank_id>/',views.question_list,name='question_list'),
    # path('question_add/<int:question_bank_id>/',views.question_add,name='question_add'),
    # path('question_add_batch/<int:question_bank_id>/',views.question_add_batch,name='question_add_batch'),

    # path('contest_manage',views.contest_manage,name='contest_manage'),
    # path('contest_create',views.contest_create,name='contest_create'),
    # path('contest_config/<int:contest_id>/',views.contest_config,name='contest_config'),
    # path('contest/<int:contest_id>/',views.contest,name='contest')
    
]