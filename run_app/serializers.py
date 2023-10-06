from rest_framework import serializers
from django.core.validators import MinLengthValidator
from .models import Training, Feedback
from django.contrib.auth.models import User


class TrainingSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[MinLengthValidator(2)])
    
    class Meta:
        model = Training
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feedback
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
