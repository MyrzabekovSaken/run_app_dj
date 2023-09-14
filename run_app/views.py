from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import TrainingSerializer
from .models import Training


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all().order_by('date')
    serializer_class = TrainingSerializer

    filter_backends = [
        # DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter,
        ]

    # filterset_fields = {}
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'date']
