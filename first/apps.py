from django.apps import AppConfig


class FirstConfig(AppConfig):
    name = 'first'

    def ready(self):
        import first.signals
