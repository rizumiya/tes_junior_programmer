from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.tampilan_get_api, name='api')
]