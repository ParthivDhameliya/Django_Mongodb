from django.db import models

# Create your models here.

class businessModel(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=20)
    businessName = models.CharField(max_length=70)
    businessLocation = models.CharField(max_length=100)
    businessCategory = models.CharField(max_length=70)
    businessDescription = models.CharField(max_length=200, blank = True, default="N/A")
    image = models.ImageField(upload_to='business/images')

    def __str__(self):
        return self.businessName