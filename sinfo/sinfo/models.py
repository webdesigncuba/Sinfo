# Django
from django.db import models
from django.conf import Settings, settings


class BaseModel(models.Model):
    user_creation = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_creation')
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update')
    date_update = models.DateTimeField(auto_now_add=True)3

    class Meta:
        abstract = True