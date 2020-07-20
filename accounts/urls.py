from django.urls import path
from .views import SignUpView, Account
from . import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home/', Account.home, name='home'),
    path('results/', views.results)
]


