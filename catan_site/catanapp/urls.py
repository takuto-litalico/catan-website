from django.urls import path
from . import views

app_name = "catanapp"
urlpatterns = [
    path('', views.index, name='index')
]