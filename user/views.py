from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Stock
from .serializers import RegistrationSerializer, StockSerializer
from .permissions import IsAdminOrOwner
from rest_framework.response import Response
from rest_framework.views import APIView

class Registration(APIView):
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid():
            account = serializer.save(data)
            return Response({"detail": "Successfully registered.", "username": account.username, "email": account.email}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        print(user)
        if user.is_authenticated:
            print("User is authenticated")
            refresh_token = RefreshToken.for_user(user)
            refresh_token.blacklist()
            print("Logged out")
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "User not authenticated."}, status=status.HTTP_401_UNAUTHORIZED)

class StockListCreateView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdminOrOwner]

    def create(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            # Return a custom response if the user is not authenticated
            return Response({"error": "You must be logged in to create a stock."}, status=status.HTTP_403_FORBIDDEN)
        
        # Proceed with the normal flow if the user is authenticated
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class StockRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAdminOrOwner]
