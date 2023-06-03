from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.home,name='home'),
    # path("about/", views.about, name='about'),
    path("", views.signup, name='signup'),
    path("login/", views.login, name='login'),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("logout/", views.logout, name='logout'),
    path("addevent/", views.addevent, name='addevent'),
    # path("addpost/", views.add_post, name='addpost'),
    # path("updatepost/<int:id>/", views.update_post, name='updatepost'),
    # path("deletepost/<int:id>/", views.delete_post, name='deletepost'),
]
