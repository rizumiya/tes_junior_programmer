from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.create_new_data, name='create_new')
]
