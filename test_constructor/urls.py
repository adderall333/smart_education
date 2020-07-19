from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('test/', views.new_test),
    path('add_test/', views.add_test),
    path('add_question/', views.add_question),
    path('test/edit/', views.edit),
    path('test/delete/', views.delete)
]