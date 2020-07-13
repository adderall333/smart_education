from django.contrib import admin
from django.urls import path, include

# Отслеживание url адресов
# если пользователь перейдет на какую-то страничку, то покажем ему один определенный шаблон


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
