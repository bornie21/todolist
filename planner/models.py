from django.db import models


class Planner(models.Model):
    class Meta:
        title = models.CharField(max_length=50)
        notes = models.TextField()
        deadline = models.DateTimeField()
        completed = models.BooleanField()
