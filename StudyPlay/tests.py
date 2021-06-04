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
    def test_Child_Good(self):
        item=ChildModel()
        item.ID=1
        item.Pseudo='keke'
        item.Password='123456'
        item.Age='10'
        item.Email='david@gmail.com'
        item.ParentsPseudo='samo'
        item.save()
        record=ChildModel.objects.get()
        print('____CHILD TEST ENTER GOOD____')
        self.assertEqual(item.Pseudo, 'keke')
        self.assertEqual(record, item)
         
    def test_Child_NGood(self):
        item=ChildModel()
        item.ID=1
        item.Pseudo='dd'
        item.Password='11'
        item.Age='ds'
        item.Email='davidgmail'
        item.ParentsPseudo='samo'
        item.save()
        record=ChildModel.objects.get()
        print('____CHILD TEST NO ENTER GOOD____')
        self.assertEqual(item.Pseudo, 'dd')
        self.assertNotEqual(record, item)
    
class Parentstest(TestCase):
    def test_Parent_Good(self):
        item=ParentsModel()
        item.ID=1
        item.Pseudo='keke'
        item.Password='1236'
        item.Email='davidgmail.com'
        item.Country='France'
        item.save()
        record=ParentsModel.objects.get()
        print('______WORK TEST PARENTS GOOD ENTER______')
        self.assertEqual(item.Pseudo, 'keke')
        self.assertEqual(record, item)

    def test_Parent_NGood(self):
        item=ParentsModel()
        item.ID=1
        item.Pseudo='dd'
        item.Password='1236'
        item.Email='davidgmail.com'
        item.Country='France'
        item.save()
        record=ParentsModel.objects.get()
        print('______WORK TEST PARENTS NO GOOD ENTER______')
        self.assertEqual(item.Pseudo, 'dd')
        self.assertNotEqual(record, item)

class Admintest(TestCase):
    def test_Admin_Good(self):
        item=AdminModel()
        item.ID=1
        item.Adminid='keke'
        item.Password='123456'
        item.Email='davidgmail.com'
        item.save()
        record=AdminModel.objects.get()
        print('______ADMIN TEST GOOD ENTER______')
        self.assertEqual(item.Adminid, 'keke')
        self.assertEqual(record, item)

    def test_Admin_NGood(self):
        item=AdminModel()
        item.ID=1
        item.Adminid='dd'
        item.Password='123456'
        item.Email=111
        item.save()
        record=AdminModel.objects.get()
        print('______ADMIN TEST NO GOOD ENTER______')
        self.assertEqual(item.Adminid, 'dd')
        self.assertNotEqual(record, item)

class Workerstest(TestCase):
    def test_Workers_Good(self):
        item=WorkersModel()
        item.ID=1
        item.Workerid='keke'
        item.Password='16'
        item.Email='davidgmail.com'
        item.type='Front-end'
        item.save()
        record=WorkersModel.objects.get()
        print('______WORK TEST WORKER GOOD ENTER______')
        self.assertEqual(item.Workerid, 'keke')
        self.assertEqual(record, item)
    def test_Workers_NGood(self):
        item=WorkersModel()
        item.ID=1
        item.Workerid='dd'
        item.Password='16'
        item.Email=11
        item.type='kk'
        item.save()
        record=WorkersModel.objects.get()
        print('______WORK TEST WORKER NO GOOD ENTER______')
        self.assertEqual(item.Workerid, 'dd')
        self.assertNotEqual(record, item)

class Activitiestest(TestCase):
    def test_Activities_Good(self):
        item=ActivitiesModel()
        item.ID=1
        item.Name='Puzzle'
        item.Subject='Funny'
        item.Link='/StudyPlay/ExPuzzle'
        item.save()
        record=ActivitiesModel.objects.get()
        print('______DATA TEST Activities GOOD ENTER______')
        self.assertEqual(item.Name, 'Puzzle')
        self.assertEqual(record, item)
    def test_Workers_NGood(self):
        item=ActivitiesModel()
        item.ID=1
        item.Name='Puzzle'
        item.Subject=11
        item.Link='/StudyPlay/ExPuzzle'
        item.save()
        record=ActivitiesModel.objects.get()
        print('______DATA TEST Activities NO GOOD ENTER______')
        self.assertEqual(item.Name, 'Puzzle')
        self.assertNotEqual(record, item)

class Countriestest(TestCase):
    def test_Countries_Good(self):
        item=CountriesModel()
        item.ID=1
        item.Name='Israel'
        item.Count=1
        item.save()
        record=CountriesModel.objects.get()
        print('______DATA TEST Countries GOOD ENTER______')
        self.assertEqual(item.Name, 'Israel')
        self.assertEqual(record, item)
    def test_Countries_NGood(self):
        item=CountriesModel()
        item.ID=1
        item.Name='France'
        item.Count='1'
        item.save()
        record=CountriesModel.objects.get()
        print('______DATA TEST Activities NO GOOD ENTER______')
        self.assertEqual(item.Name, 'France')
        self.assertNotEqual(record, item)

class Reviewstest(TestCase):
    def test_Reviews_Good(self):
        item=ReviewsModel()
        item.ID=1
        item.Description='I have funny moment'
        item.Ratings=1
        item.save()
        record=ReviewsModel.objects.get()
        print('______DATA TEST Reviews GOOD ENTER______')
        self.assertEqual(item.ID, 1)
        self.assertEqual(record, item)
    def test_Reviews_NGood(self):
        item=ReviewsModel()
        item.ID=1
        item.Description='I have funny moment'
        item.Ratings='1'
        item.save()
        record=ReviewsModel.objects.get()
        print('______DATA TEST Reviews NO GOOD ENTER______')
        self.assertEqual(item.ID, 1)
        self.assertNotEqual(record, item)

class Reviewstest(TestCase):
    def test_ActivityDone_Good(self):
        item=ActivityDoneModel()
        item.ID=1
        item.NameAct='Puzzle'
        item.PseudoC='ccc'
        item.PseudoP='ppp'
        item.Grade='5'
        item.NumOfGame=4
        item.save()
        record=ActivityDoneModel.objects.get()
        print('______DATA TEST ActivityDone GOOD ENTER______')
        self.assertEqual(item.NameAct, 'keke')
        self.assertEqual(record, item)
    def test_ActivityDone_NGood(self):
        item=ActivityDoneModel()
        item.ID=1
        item.NameAct='Memory'
        item.PseudoC='ccc'
        item.PseudoP='ppp'
        item.Grade='5'
        item.NumOfGame='4'
        item.save()
        record=ActivityDoneModel.objects.get()
        print('______DATA TEST ActivityDone NO GOOD ENTER______')
        self.assertEqual(item.NameAct, 'Memory')
        self.assertNotEqual(record, item)

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)
        
    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
  