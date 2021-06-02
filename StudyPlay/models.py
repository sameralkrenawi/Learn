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
    ID = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    Pseudo= models.CharField(db_column='Pseudo',max_length=10)
    Password = models.CharField(db_column='Password',max_length=10)
    Age= models.TextField(db_column='Age')
    Email= models.TextField(db_column='Email')
    ParentsPseudo= models.CharField(db_column='ParentsPseudo',default=None,max_length=10)
    profile_pic = models.ImageField(u"profile1.png",blank=True,default=None,upload_to="static/images/")
    class Meta:
        managed = True
        db_table = 'child'


class WorkersModel(models.Model):  
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
    ID = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    Pseudo= models.CharField(db_column='Pseudo',max_length=10)
    Password = models.CharField(db_column='Password',max_length=100)
    Email= models.TextField(db_column='Email')
    country= models.TextField(db_column='country')
    profile_pic = models.ImageField(u"profile1.png",blank=True,default=None,upload_to="static/images/")
    class Meta:
        managed = True
        db_table = 'Parents'

class ActivitiesModel(models.Model):
    ID = models.IntegerField(db_column='ID',default=None,primary_key=True) 
    Name = models.CharField(db_column='Name',max_length=100)
    Subject = models.CharField(db_column='Subject',max_length=100)
    Link = models.CharField(db_column='Link',default=None,max_length=100)
    class Meta:
        managed = True
        db_table = 'activities'

class CountriesModel(models.Model):
    ID = models.IntegerField(db_column='ID',default=None,primary_key=True) 
    Name = models.CharField(db_column='Name',default=None,max_length=100)
    Count = models.IntegerField(db_column='Count',default=0)
    class Meta:
        managed= True
        db_table='countries'

class ReviewsModel(models.Model):
    ID = models.IntegerField(db_column='ID',default=None,primary_key=True) 
    Description = models.CharField(db_column='Description',default=None,max_length=100)
    Ratings = models.IntegerField(db_column='Ratings')
    class Meta:
        managed= True
        db_table='reviews'

class ActivityDoneModel(models.Model):
    ID = models.IntegerField(db_column='ID',default=None,primary_key=True) 
    NameAct = models.CharField(db_column='NameAct',default=None,max_length=100)
    PseudoC = models.CharField(db_column='PseudoC',default=None,max_length=100)
    PseudoP = models.CharField(db_column='PseudoP',default=None,max_length=100)
    Grade = models.CharField(db_column='Grade',default=None,max_length=100)
    NumOfGame = models.IntegerField(db_column='NumOfGame',default=1)
    class Meta:
        managed= True
        db_table='activityDone'