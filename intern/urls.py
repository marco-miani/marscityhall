from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_intern, name='view_intern'),
]
