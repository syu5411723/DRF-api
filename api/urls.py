from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import VideoViewSet, CreateUserView

router = routers.DefaultRouter()
router.register('videos', VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create', CreateUserView.as_view(), name='create'),
]