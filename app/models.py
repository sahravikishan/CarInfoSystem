from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

def validator_email(value):
    if '@gmail.com' in value:
        return value
    else:
        raise ValidationError("Enter a Gmail ID")

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=200, validators=[validator_email])
    password = models.CharField(max_length=128)  # Increased to support hashed passwords
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def set_password(self, raw_password):
        """Hash and set the password using Django's password hashing"""
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        """Check if the given password matches the stored hash"""
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['-created_at']