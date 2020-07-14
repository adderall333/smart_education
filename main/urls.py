from django.urls import path
from . import views

# отслеживаем куда всё же перешел пользователь
# в зависимости от того куда он перешел будем вызывать функцию из файла views
# а функция будет показывать определенный html код


urlpatterns = [
    path('', views.menu),
    path('sign-in', views.signin),
    path('sign-up', views.signup),
]