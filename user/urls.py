from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import StockListCreateView, StockRetrieveUpdateDestroyView, Logout, Registration

urlpatterns = [
    path('register/', Registration.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', Logout.as_view(), name='logout'),
    path('stocks/', StockListCreateView.as_view(), name='stocks-list-create'),
    path('stocks/<int:pk>/', StockRetrieveUpdateDestroyView.as_view(), name='stocks-retrieve-update-destroy'),
]
