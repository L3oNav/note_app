from django.db import models
from django.contrib.auth.models import AbstractUser
from utils import BaseModel


# Create your models here.
class User(BaseModel, AbstractUser):

    email = models.EmailField(
        "email address",
        unique=True,
        error_messages = {
            "unique": "username is already in use",
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    is_verified = models.BooleanField('verified', default=False, help_text=(
        "set to true when the user have verified it\'s email address."
    ))

    def __str__(self):
        return self.username
