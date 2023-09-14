from rest_framework import serializers
from django.core.validators import MinLengthValidator
from .models import Training


class TrainingSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[MinLengthValidator(2)])
    class Meta:
        model = Training
        fields = '__all__'
