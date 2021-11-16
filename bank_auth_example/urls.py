from django.contrib import admin
from django.urls import path, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from auth_example import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/',         admin.site.urls),
    path('login/',         TokenObtainPairView.as_view()),
    path('refresh/',       TokenRefreshView.as_view()),
    path('verifyToken/',   views.VerifyTokenView.as_view()),
    path('user/',          views.UserCreateView.as_view()),
    path('user/getMyInfo/<int:pk>/', views.UserDetailView.as_view()),
    path('user/updateUser/<int:pk>/', views.UserUpdateView.as_view()),
    path('user/deleteUser/<int:pk>/', views.UserDeleteView.as_view()),
    path('user/deactiveUser/<int:pk>/', views.UserDeactiveView.as_view()),

    # Swagger urls
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
