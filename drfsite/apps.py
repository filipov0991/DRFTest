from django.apps import AppConfig
from django.apps import AppConfig


class DrfsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drfsite'

    def ready(self):
        import drfsite.signals

    