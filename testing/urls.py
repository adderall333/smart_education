from django.urls import path
from . import views

urlpatterns = [
    path('', views.enter_code),
    path('open_test/', views.open_test),
    path('run_test/', views.run_test)
]