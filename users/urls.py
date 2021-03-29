from django.urls import path
from users.views import SignupView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path('token/verify/', TokenVerifyView.as_view(), name="verify"),
]

urlpatterns += [
    path('signup/', SignupView.as_view(), name="signup"),
]


