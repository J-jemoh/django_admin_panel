
from unicodedata import name
from django.urls import path,include
from django.http import HttpResponse
from . import views

urlpatterns = [
path('',views.home, name="home"),
path('register',views.register, name="register"),
path('dashboard/admin',views.dashboard,name="dashboard"),
path('logout',views.logout_view, name="logout"),
path('dashboard/participants',views.participnats, name="participants"),
path('dashboard/participants/add',views.new_participants,name="add-participants"),
path('dashboard/partipicipants/all',views.all_participants,name="new_participants"),
path('dashboard/participant/<int:id>',views.view_participant, name="show_participants"),
path('dashboard/participant/viral_load/<int:id>',views.viralloads,name="viralload"),
path('dashboard/participants/high_viral_loads',views.highvl,name="highvl"),
path('dashboard/participants/high_viral_loads/<int:id>',views.rerandview,name="rerandview"),
path('dashboard/participants/rerands/all',views.all_rerand,name="all_rerand"),
path('dashboard/participants/rerand/all/<int:id>',views.month6,name="eoic_participant"),
path('dashboard/participants/month6/all',views.allmonth6,name="all_month6"),
]
