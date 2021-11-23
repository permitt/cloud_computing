from django.db import models


# Create your models here.
class EmployeeModel(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    birth_date = models.DateTimeField()
    salary = models.FloatField()
