from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.enter_code),
    path('open_test/', views.open_test),
    re_path(r'^(run_test/send/(?P<code>\d+)/(?P<questions_number>\d+)/)', views.send_answers),
    path('run_test/', views.run_test)
]
