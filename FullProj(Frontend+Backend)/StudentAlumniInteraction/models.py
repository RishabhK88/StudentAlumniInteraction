from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Alumni(models.Model):
    username = models.TextField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=32)
    BRANCH_CHOICES = (
    ("coe", "COE"),
    ("ece", "ECE"),
    ("mech", "Mech"),
    )

    branch = models.CharField(max_length=9,
                  choices=BRANCH_CHOICES,
                  default="coe")
    l = models.TextField(max_length=200)


