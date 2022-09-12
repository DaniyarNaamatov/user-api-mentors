from django.urls import path, include, re_path
from .views import LoginAPIView, RegisterView, VerifyEmail
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)


ROUTER = DefaultRouter()
ROUTERCARD = DefaultRouter()




urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("verify/", VerifyEmail.as_view(), name="email-verify"),
    path("auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    path("token/", TokenObtainSlidingView.as_view(), name="token_obtain"),
    path("refresh/", TokenRefreshSlidingView.as_view(), name="token_refresh"),
]