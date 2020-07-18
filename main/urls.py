from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu),
    path('sign-in', views.signin),
    path('sign-up', views.signup),
]