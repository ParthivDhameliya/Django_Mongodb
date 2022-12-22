from django.contrib import admin
from .models import businessModel

# Register your models here.

@admin.register(businessModel)
class businessAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email', 'mobile', 'password', 'businessName', 'businessLocation', 'businessCategory', 'businessDescription','image')
