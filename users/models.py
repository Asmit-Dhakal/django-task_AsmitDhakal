from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from datetime import date, timedelta
class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, membership_type=None,**extra_fields):
        if not phone_number:
            raise ValueError("Phone number is required")
        if membership_type:
            extra_fields.setdefault("membership_start_date", date.today())
            extra_fields.setdefault("membership_expiry_date", self.calculate_expiry_date(membership_type))

        extra_fields.setdefault("is_active", True)
        user = self.model(phone_number=phone_number, membership_type=membership_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def calculate_expiry_date(self, membership_type):
        durations = {
            "Silver": 10,
            "Gold": 20,
            "Diamond": 30
        }
        return date.today() + timedelta(days=durations.get(membership_type, 30))

class User(AbstractBaseUser):
    MEMBERSHIP_CHOICES = [("Silver", "Silver"), ("Gold", "Gold"), ("Diamond", "Diamond")]
    phone_number = models.CharField(max_length=15, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    membership_type = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, blank=True, null=True)
    membership_start_date = models.DateField(blank=True, null=True)
    membership_expiry_date = models.DateField(blank=True, null=True)
    objects = UserManager()
    USERNAME_FIELD = "phone_number"
    def __str__(self):
        return f"{self.phone_number} - {self.membership_type if self.membership_type else 'No Membership'}"
