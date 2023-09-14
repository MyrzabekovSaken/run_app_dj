from django.db import models


class Training(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Training'
        verbose_name_plural = 'Trainings'
