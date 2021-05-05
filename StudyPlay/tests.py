from django import urls
from django.db.models.fields import AutoField
from django.test import TestCase,SimpleTestCase
from django.urls import resolve, reverse
from StudyPlay.views import *
from StudyPlay.models import *
import unittest


class TestUrls(unittest.TestCase):
    def testd(self):
        url1=reverse('index')
        url2=reverse('ErrorPage')
        url3=reverse('index')
        url4=reverse('InformClient')
        url5=reverse('sendemail')
        url6=reverse('contact')
        url7=reverse('changepassword')
        print(resolve(url1))
        print(resolve(url2))
        print(resolve(url3))
        print(resolve(url4))
        print(resolve(url5))
        print(resolve(url6))
        print(resolve(url7))
        print('______WORK TEST URL ______')


        
class Childtest(TestCase):
    def test_Child(self):
        item=ChildModel()
        item.ID=1
        item.Pseudo='keke'
        item.Password='123456'
        item.Age='10'
        item.Email='david@gmail.com'
        item.ParentsPseudo='samo'
        item.save()
        record=ChildModel.objects.get()
        print('______WORK TEST CHILD GOOD ENTER______')
        self.assertEqual(item.Pseudo, 'keke')
        self.assertEqual(record, item)

class Parentstest(TestCase):
    def test_Parents(self):
        item=ParentsModel()
        item.ID=1
        item.Pseudo='keke'
        item.Password='123456'
        item.Email='davidgmail.com'
        item.Country='France'
        item.save()
        record=ParentsModel.objects.get()
        print('______WORK TEST PARENTS NO GOOD ENTER______')

        self.assertEqual(item.Pseudo, 'keke')
        self.assertEqual(record, item)
  