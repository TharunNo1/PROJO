from django.urls import path 
from .views import SignUpView, HelloUserView, ProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh', TokenRefreshView.as_view(), name="token_refresh"),
    path('hello/', HelloUserView.as_view(), name="hello_user" ),
    path('profile/', ProfileView.as_view(), name='profile'),
]