from django.urls import path
from . import views
urlpatterns=[
    path('reg',views.reg_view,name='reg'),
    path('login',views.login_view,name='login')
]