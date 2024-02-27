from .models import Stock
from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
    
    def save(self, validated_data):
        password = validated_data['password']
        password2 = validated_data['password2']
        email = validated_data.get('email')
        if not email:
            raise serializers.ValidationError({'error': 'Email is required.'})

        if password != password2:
            raise serializers.ValidationError({'error': 'Passwords must match.'})
        
        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email is already in use.'})
        
        account = User(email=validated_data['email'], username=validated_data['username'])
        account.set_password(password)
        account.save()
        
        return account
    
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'name', 'mobile', 'email', 'blood_group', 'age', 'weight', 'state', 'district', 'city', 'pin']