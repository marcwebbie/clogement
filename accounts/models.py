from django.db import models
from django.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    photo = models.URLField()
