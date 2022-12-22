from django.db import models

# Create your models here.

class userModel(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=70)
    mobile = models.BigIntegerField(blank=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    password = models.CharField(max_length=20, default=' ', blank=False)

    def __str__(self):
        return self.firstName+' '+self.lastName