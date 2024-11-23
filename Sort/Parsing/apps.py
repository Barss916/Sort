from django.apps import AppConfig

from Parsing.models import Product


class ParsingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Parsing'

