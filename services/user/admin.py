from django.contrib import admin
from .models import userModel

# Register your models here.

@admin.register(userModel)
class userAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'mobile', 'city', 'country', 'zipcode')
