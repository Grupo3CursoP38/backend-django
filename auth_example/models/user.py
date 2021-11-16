from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Todo cliente debe tener un username.")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.IntegerField(primary_key=True, unique=True)
    email = models.EmailField('Email',   max_length=100, unique=True)
    name = models.CharField('name',     max_length=45)
    lastname = models.CharField('lastname', max_length=50)
    phone = models.CharField("phone", max_length=20)
    birthdate = models.DateField("birthdate")
    is_active = models.BooleanField("is_active", default=True)
    password = models.CharField('Password', max_length=256)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'email'
