from django.urls import path
from account.views import user_list_view, user_detail_view

urlpatterns = [
    path('', user_list_view, name='user-list'),
    path('<int:pk>/', user_detail_view, name='user-detail'),
]