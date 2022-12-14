from django.db import models

from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

from phonenumber_field.modelfields import PhoneNumberField



class MyUserManager(BaseUserManager):
    def _create_user(self, email, username, password, phone, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели Email")
        if not username:
            raise ValueError("Вы не ввели Логин")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password, phone):
        return self._create_user(email, username, password, phone)

    def create_superuser(self, email, username, password, phone):
        return self._create_user(
            email, username, password, phone, is_staff=True, is_superuser=True
        )


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    photo = models.ImageField(
        default="media/user.png", upload_to="media/", blank=True)

    phone = PhoneNumberField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["email", "username"]
    objects = MyUserManager()


    class Meta:
        verbose_name = "Абонент"
        verbose_name_plural = "Абоненты"

    def __str__(self):
        return self.email
