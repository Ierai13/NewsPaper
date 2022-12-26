from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '_accounts'

    def ready(self):
        import _accounts.signals
