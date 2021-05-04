from django import urls
from django.db.models.fields import AutoField
from django.test import TestCase,SimpleTestCase
from django.urls import resolve, reverse
from StudyPlay.views import *
from StudyPlay.models import *
import unittest
from django.test.client import RequestFactory


class TestUrls(unittest.TestCase):

    def testd(self):
        url2=reverse('registerformchild')
        url3=reverse('registerformparents')
        url4=reverse('ErrorPage')
        url5=reverse('index')
        url6=reverse('after_approuval_worker_insert')
        url7=reverse('get_new_workers_table')
        url9=reverse('get_new_child_table/<str:userid>/')
        url10=reverse('get_child_table/<str:userid>/')
        url12=reverse('get_child_connection/<str:userid>/')
        url13=reverse('Deletechild')
        url14=reverse('sendemail')
        url15=reverse('contact')
        url16=reverse('changepassword')
        url17=reverse('after_approuval_child_insert')
        url18=reverse('InformClient')
        url19=reverse('login')
        url20=reverse('Deleteworker')

        print(resolve(url2))
        print(resolve(url3))
        print(resolve(url4))
        print(resolve(url5))
        print(resolve(url6))
        print(resolve(url7))
        print(resolve(url9))
        print(resolve(url10))
        print(resolve(url12))
        print(resolve(url13))
        print(resolve(url14))
        print(resolve(url15))
        print(resolve(url16))
        print(resolve(url17))
        print(resolve(url18))
        print(resolve(url19))
        print(resolve(url20))
