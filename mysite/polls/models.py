#! /usr/bin/env python
#coding=utf-8

from __future__ import unicode_literals
import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# class userModel(models.Model):
#     nickName = models.CharField(max_length=10)
#     level = models.TextField()
#     vip = models.TextField()
#     # strengthen
#     # gen
#     # gold



#管理类
class UserManager(BaseUserManager):

    #创建user
    def create_user(self,phone, password=None):
        user = self.model(
            phone = phone,
            uuid = str(uuid.uuid1()),
        )

        user.set_password(password)
        user.uuid = str(uuid.uuid1())
        user.save(using=self._db)
        return user

    #创建超级管理员
    def create_superuser(self,phone,  password):

        user = self.create_user(
            phone = phone,
            password = password
        )
        user.uuid = str(uuid.uuid1())
        user.is_staff = True
        user.is_active = True
        user.is_admin = True
        user.is_superuser=True
        user.save(using=self._db)
        return user

#通行证
class MyUser(AbstractBaseUser,PermissionsMixin):

    uuid = models.CharField(max_length=36,unique=True, db_index=True)
    phone = models.CharField(max_length=11, unique=True)
    username = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    #有该字段创建的superuser才具有admin编辑权限
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'phone'
    # REQUIRED_FIELDS = ['phone']
    objects = UserManager()

    def get_short_name():
        return self.phone

    def has_perm(self, perm, obj=None):
        if self.is_active and self.is_superuser:
            return True

# passport.objects.create_user(email,username,password)  注册用户用法
# passportObj = auth.authenticate(username = username, password = password) 验证用户用法