from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = "main"

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('/<int:id>', Product.as_view(), name='product'),
    path('categories/', categories, name='categories'),
    path('filter/', Filtering.as_view(), name='filter'),
    path('filter/cheaper', FilteringLower.as_view(), name='filter_lower'),
    path('filter/expensive', FilteringHigher.as_view(), name='filter_lower'),
]

