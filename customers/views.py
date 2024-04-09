from rest_framework import viewsets, generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Plan
from accounts.models import CustomUser
from .serializers import PlanSerializer, CustomerSerializer, UserProfileSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = CustomUser.objects.all()
    serializer_class = CustomerSerializer

class PlanListCreateAPIView(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

class PlanRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)
    def get(self, request, *args, **kwargs):
        queryset = CustomUser.objects.values('username','email','dob', 'plan__name').get(username=request.user.username)
        # print(serializer_class.data)
        return Response(
            data={
                "status_code": status.HTTP_200_OK,
                "message": "Success",
                "data": queryset,
            },
        )

    def post(self, request):
        plan = request.data.get("plan", 0)
        # plan_obj = Plan.objects.get(id=int(plan))
        # CustomUser.objects.get(username=request.user.username).update(**{plan:plan_obj})
        user_instance = get_object_or_404(CustomUser, username=request.user.username)

        # Retrieve the plan object using plan_obj_id (assuming you have a Plan model)
        plan_obj = get_object_or_404(Plan, pk=plan)

        # Update the user's plan
        user_instance.plan = plan_obj
        user_instance.save()
        # user.plan = plan_obj
        # user.save()
        return Response(
            data={
                "status_code": status.HTTP_200_OK,
                "message": "Success",
                "data": "Plan Updated",
            },
        )
    # def get(self, request, *args, **kwargs):
    #     print(request)
    # queryset = Plan.objects.all()
    # serializer_class = PlanSerializer

# class CustomUserUpdatePlanAPIView(generics.UpdateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer