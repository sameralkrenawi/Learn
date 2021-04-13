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


<<<<<<< HEAD
class ChildModel(models.Model):
=======
class ChildModel(models.Model):    
    ID = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
>>>>>>> bea6460f15442bc9f021e2cbe2124cc408b7c0ba
    Pseudo= models.CharField(db_column='Pseudo',max_length=10)
    Password = models.CharField(db_column='Password',max_length=100)
    Age= models.TextField(db_column='Age')
    Email= models.TextField(db_column='Email')
    ParentsPseudo= models.CharField(db_column='ParentsPseudo',max_length=100)
    class Meta:
        managed = True
        db_table = 'child'


class WorkersModel(models.Model):
<<<<<<< HEAD
=======
    
>>>>>>> bea6460f15442bc9f021e2cbe2124cc408b7c0ba
    ID = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    Workerid= models.CharField(db_column='Workerid',max_length=10)
    Pseudo= models.CharField(db_column='Pseudo',max_length=10)
    Password = models.CharField(db_column='Password',max_length=4)
    Email= models.TextField(db_column='Email')
    type= models.TextField(db_column='type')
    class Meta:
        managed = True
        db_table = 'workers'


class ParentsModel(models.Model):
<<<<<<< HEAD
=======
    ID = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
>>>>>>> bea6460f15442bc9f021e2cbe2124cc408b7c0ba
    Pseudo= models.CharField(db_column='Pseudo',max_length=10)
    Password = models.CharField(db_column='Password',max_length=100)
    Email= models.TextField(db_column='Email')
    class Meta:
        managed = True
        db_table = 'Parents'

class ActivitiesModel(models.Model):
    Name = models.CharField(db_column='Name',max_length=100)
    Subject = models.CharField(db_column='Subject',max_length=100)
    class Meta:
        managed = True
        db_table = 'activities'
