from django.urls import path
from . import views
app_name ='content_ms'

urlpatterns = [
    path('', views.show_genres,name='genre'),
]