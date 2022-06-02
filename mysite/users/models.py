from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): # 유저
    student_id = models.CharField(max_length=10) # 학번