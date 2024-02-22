from django.urls import path,include
from user.views import UserList, UserDetails

urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserDetails.as_view(), name='user-detail'),
]