from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('hospital', 'Hospital'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='patient')
    
    
# Create your models here.
