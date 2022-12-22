from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="businesshome"),
    path('businessPR/', views.businessPR, name='businessPR'),
    path('businessRegistration', views.businessR, name='businessRegistration'),
    path('businessLogin', views.businessL, name='businessLogin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
