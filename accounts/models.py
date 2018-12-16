import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, is_admin, **extra_fields):
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(email=email,
                          first_name=first_name,
                          last_name=last_name,
                          is_admin=is_admin,
                          is_active=True,
                          last_login=now,
                          date_created=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, first_name='', last_name='', is_admin=False, **extra_fields):
        return self._create_user(email, password, first_name, last_name, is_admin, **extra_fields)


class User(AbstractBaseUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_last_edited = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    objects = MyUserManager()

    class Meta:
        """Extra model properties."""

        ordering = ['date_created']

    def __str__(self):
        """
        Unicode representation for an user model.

        :return: string
        """
        return self.email
