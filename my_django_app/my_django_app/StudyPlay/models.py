from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class AdminModel(models.Model):
    ID = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    Adminid = models.CharField(db_column='Adminid', max_length=9)  # Field name made lowercase.
    Pseudo= models.CharField(db_column='Pseudo',max_length=10)
    Password = models.CharField(db_column='Password',max_length=10)
    Email= models.TextField(db_column='Email')
    class Meta:
        managed = True
        db_table = 'admin'


class ChildModel(models.Model):
    Pseudo= models.CharField(db_column='Pseudo',max_length=10)
    Password = models.CharField(db_column='Password',max_length=4)
    Email= models.TextField(db_column='Email')
    class Meta:
        managed = True
        db_table = 'Child'
