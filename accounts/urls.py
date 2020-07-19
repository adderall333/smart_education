from django.urls import path
from .views import SignUpView, Account
from django.contrib.auth import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home/', Account.home, name='home'),
    # path('<int:test_id>/', Account.test, name='test'),
]


