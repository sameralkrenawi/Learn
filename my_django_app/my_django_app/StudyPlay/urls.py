
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Test', views.MainDashBoard, name='main'),
    path('registerform', views.registerform) ,
    path('registerform', views.registerFormChild)
    ]
