from django.db import models
from django.core.exceptions import ValidationError

def validator_email(value):
    if '@gmail.com' in value:
        return value
    else:
        raise ValidationError("Enter a Gmail ID")

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=200,validators = [validator_email])
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username