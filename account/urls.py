from django.urls import path
from account.views import user_list_view, user_detail_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # simplejwt views
    path("token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token-refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    # my views
    path("", user_list_view, name="user-list"),
    path("<int:pk>/", user_detail_view, name="user-detail"),
]