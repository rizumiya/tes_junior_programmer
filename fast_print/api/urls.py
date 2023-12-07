from django.urls import path

from . import views

urlpatterns = [
    path('', views.cek_data, name=''),
    path('api/', views.api_page, name='api_page'),
    path('home/', views.MainMenu.as_view(), name='home_page'),
    path('post_api/', views.save_to_database, name='save_to_database')
]