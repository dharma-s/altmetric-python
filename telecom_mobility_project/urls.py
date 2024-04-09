# telecom_mobility_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from customers.views import CustomerViewSet, PlanListCreateAPIView, PlanRetrieveUpdateDestroyAPIView #, CustomUserUpdatePlanAPIView
from accounts.views import register_user, login
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
# router.register(r'plans', PlanViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Test API",
        default_version='v1',
        description="API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/plans/', PlanListCreateAPIView.as_view(), name='plan-list-create'),
    path('api/plans/<int:pk>/', PlanRetrieveUpdateDestroyAPIView.as_view(), name='plan-detail'),
    # path('api/users/<int:pk>/update-plan/', CustomUserUpdatePlanAPIView.as_view(), name='user-update-plan'),
    path('api-token-auth/', login, name='api_token_auth'), 
    path('api/register/', register_user, name='register_user'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
