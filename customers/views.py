from rest_framework import viewsets, generics
from .models import Plan
from accounts.models import CustomUser
from .serializers import PlanSerializer, CustomerSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomerSerializer

class PlanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlanRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

# class CustomUserUpdatePlanAPIView(generics.UpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer