from django.db import models

# Create your models here.
class Intern(models.Model):
    internNumber = models.PositiveIntegerField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    graduateCourse = models.CharField(max_length=50)
    startContract = models.DateField()
    endContract = models.DateField()

def __str__(self):
    return f'Intern: {self.firstName} {self.lastName}'
