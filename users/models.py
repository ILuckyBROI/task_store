from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='base_image', null=True, blank=True)

    def safe_active(self):
        self.is_active = True
        self.save()

    def safe_delete(self):
        self.is_active = False
        self.save()
