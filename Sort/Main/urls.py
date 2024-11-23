from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories')
]

