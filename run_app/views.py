from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TrainingSerializer, FeedbackSerializer, UserSerializer
from .models import Training, Feedback, User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



User = get_user_model()


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all().order_by('date')
    serializer_class = TrainingSerializer

    permission_classes = [
        IsAuthenticated
    ]

    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter,
    ]

    # filterset_fields = {}
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'date']


    def get_queryset(self):
        return self.queryset.filter(client=self.request.user)

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    def perform_update(self, serializer):
        serializer.save(client=self.request.user)


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    permission_classes = [
        IsAuthenticated
    ]

    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter,
        ]

    filterset_fields = {
        'training': ['exact'],
        'client': ['exact'],
    }
    search_fields = ['feedback']
    ordering_fields = ['date']

    def get_queryset(self):
        return self.queryset.filter(client=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

    def perform_update(self, serializer):
        serializer.save(client=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
