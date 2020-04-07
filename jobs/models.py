from django.db import models

# Create your models here.
class Job(models.Model):
    Image = models.ImageField(upload_to='images/')
    Summary = models.CharField(max_length=200)


