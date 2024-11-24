from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('categories/', categories, name='categories'),
    path('filter/', Filtering.as_view(), name='filter'),
]

