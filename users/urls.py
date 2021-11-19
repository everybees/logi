from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

router = DefaultRouter(trailing_slash=False)
app_router = routers.DefaultRouter()
app_router.register('', UserViewSet, basename='user')

urlpatterns = [
    path('', include(app_router.urls)),
]
