from django.db import models


class CustomModelManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.models.DoesNotExsit:
            return None
