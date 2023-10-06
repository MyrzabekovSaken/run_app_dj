from django.apps import AppConfig


class RunAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'run_app'

    def ready(self):
        import run_app.signals
        