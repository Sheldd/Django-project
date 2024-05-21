"""
Модуль джанго при создании приложения
"""

from django.apps import AppConfig


class PhysicsConfig(AppConfig):
    """Класс для работы с приложением
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "physics"
