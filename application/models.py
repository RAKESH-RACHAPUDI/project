from django.db import models

# Create your models here.
class Student(models.Model):
    PIN=models.IntegerField()
    Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=3)
    Branch=models.CharField(max_length=20)
    College=models.CharField(max_length=100)



    def __str__(self):
        return self.Name

