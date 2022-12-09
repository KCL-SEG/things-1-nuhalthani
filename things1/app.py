from django.apps import AppConfig


# Exercise 2
class ThingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'things'
