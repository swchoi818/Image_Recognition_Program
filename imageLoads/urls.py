from django.urls import path, include
from . import views

app_name = 'imageLoads'

urlpatterns = [
    path('/', views.index, name = 'index'),
]
