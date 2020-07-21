from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from . import settings


# Отслеживание url адресов
# если пользователь перейдет на какую-то страничку, то покажем ему один определенный шаблон


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('main.urls')),
    path('test_constructor/', include('test_constructor.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
