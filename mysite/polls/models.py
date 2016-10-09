from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class userModel(models.Model):
    nickName = models.CharField(max_length=10)
    level = models.TextField()
    vip = models.TextField()
    # strengthen
    # gen
    # gold
