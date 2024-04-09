from rest_framework import serializers
from .models import Plan
from accounts.models import CustomUser

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = ['username', 'email']
        fields = '__all__'
        # extra_kwargs = {'password': {'write_only': True}}
    # def create(self, validated_data):
    #     validated_data['password'] = make_password(validated_data['password'])
    #     return super().create(validated_data)