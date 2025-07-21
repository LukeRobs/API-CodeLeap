from django.db import models
from django.utils import timezone

class Career(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_datetime = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_datetime']
    
    def __str__(self):
        return self.title