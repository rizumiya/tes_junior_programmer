from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.show_home, name='home'),
    path('', views.show_default, name='/'),
]