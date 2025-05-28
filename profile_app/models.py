from django.db import models

# Create your models here.
from django.db import models

class StudentProfile(models.Model):
    name = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    year = models.IntegerField()
    gpa = models.FloatField()

    def __str__(self):
        return self.name

