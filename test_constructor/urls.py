from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_test/', views.new_test),
    path('add_test/', views.add_test),
    path('add_question/', views.add_question)
]