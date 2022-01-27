
from unicodedata import name
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
path('',views.home, name="home"),
path('register',views.register, name="register"),
path('dashboard/admin',views.dashboard,name="dashboard"),
path('logout',views.logout_view, name="logout")
]
