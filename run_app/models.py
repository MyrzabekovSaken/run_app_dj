from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class Training(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    date = models.DateField()
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.date} - {self.client}"

    class Meta:
        verbose_name = 'Training'
        verbose_name_plural = 'Trainings'

class Feedback(models.Model):
    feedback = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    training = models.OneToOneField(Training, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.feedback} - {self.training.date} - {self.client.username} - {self.training.title} - {self.date}"

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
