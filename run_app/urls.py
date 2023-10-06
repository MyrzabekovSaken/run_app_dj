from django.contrib import admin
from django.urls import path, include
from .views import TrainingViewSet, FeedbackViewSet, UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'trainings', TrainingViewSet)
router.register(r'feedbacks', FeedbackViewSet)   
router.register(r'users', UserViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
