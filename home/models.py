from django.db import models

# Create your models here.
class Booking(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    email=models.EmailField()
    phnumber=models.CharField(max_length=13)
    startdate=models.DateField()
    finishdate=models.DateField()
    country=models.CharField(max_length=50)
    subject=models.TextField()

    def __str__(self):
        return self.email