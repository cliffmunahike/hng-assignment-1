from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=200)
    github_url = models.CharField(max_length=200)
    current_datetime = models.DateTimeField()
    
    def __str__(self):
        return self.email
