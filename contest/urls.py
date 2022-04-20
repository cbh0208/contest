from django.urls import path
from . import views
urlpatterns=[
    path('bank_list',views.bank_list),
    path('bank/<int:id>/',views.bank),
    path('bank_add',views.bank_add),

    path('get_current_question/<int:id>/',views.get_current_question),
    path('question_delete',views.question_delete),
    path('question_add',views.question_add),
    path('question_add_batch',views.question_add_batch),
    path('question_edit',views.question_edit),

    path('get_contest_list',views.get_contest_list),
    path('create_contest',views.create_contest),
    path('end_contest',views.end_contest),

    path('get_contest_received',views.get_contest_received),
    path('get_contest/<int:id>/',views.get_contest),
    path('temporary_submit/<int:id>/',views.temporary_submit),
    path('contest_submit',views.contest_submit),


    path('get_grade',views.get_grade),
    path('get_detail/<int:id>/',views.get_detail),

    path('test',views.test)
]