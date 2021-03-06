
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
path('dashboard/participant/edit/<int:id>',views.edit_participant, name="edit_participant"),
path('dashboard/participant/delete/<int:id>',views.delete_participant, name="delete_participant"),
path('dashboard/participant/viral_load/<int:id>',views.viralloads,name="viralload"),
path('dashboard/participants/high_viral_loads',views.highvl,name="highvl"),
path('dashboard/participants/high_viral_loads/<int:id>',views.rerandview,name="rerandview"),
path('dashboard/participants/rerands/all',views.all_rerand,name="all_rerand"),
path('dashboard/participants/rerand/all/<int:id>',views.month6,name="eoic_participant"),
path('dashboard/participants/month6/all',views.allmonth6,name="all_month6"),
path('dashboard/participants/eoic/all',views.extended_outcome,name="all_eoic"),
path('dashboard/participants/eoic/participant/<int:id>',views.eoic_participants,name="eoic_id"),
path('dashboard/participants/eoic/participant/all/done_eoic',views.done_eoic,name="done_eoic"),
path('dashboard/participants/highvl/edit/<int:id>',views.edit_vl,name="edit_vl"),
path('dashboard/participants/rerand/edit/<int:id>',views.edit_rerand,name="edit_rerand"),
path('dashboard/participant/rerand/delete/<int:id>',views.delete_rerand, name="delete_rerand"),
path('dashboard/participant/month6/edit/<int:id>',views.edit_month6, name="edit_month6"),
path('dashboard/participant/month6/delete/<int:id>',views.delete_month6, name="delete_month6"),
path('dashboard/participant/eoic/edit/<int:id>',views.edit_eoic, name="edit_eoic"),
path('dashboard/participant/eoic/delete/<int:id>',views.delete_eoic, name="delete_eoic"),
]
