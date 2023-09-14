from django.contrib import admin
from django.urls import path, include
from .views import TrainingViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'trainings', TrainingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
