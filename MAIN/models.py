import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, password, email='123@gmail.com' ,is_active=True, is_admin=False, is_staff=False):
        if not username:
            raise ValueError('users must have an username')
        if not email:
            raise ValueError('users must have an email')
        if not password:
            raise ValueError('users must have a password')
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.username = username
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, username, password=None):
        user = self.create_user(
            username, 
            password=password,
            is_staff=True
        )

    def create_superuser(self, username, password=None):
        user = self.create_user(
            username, 
            password=password,
            is_admin=True,
            is_staff=True
        )

class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True, default='')
    email = models.EmailField(blank=True, null=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    hak_pilih = models.IntegerField(default=1, editable=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=True):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active

class Calon(models.Model):
    objects = UserManager()

    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    suara = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.username