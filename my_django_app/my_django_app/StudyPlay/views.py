from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from StudyPlay.models import AdminModel
from StudyPlay.models import ChildModel
import mysql.connector
# Create your views here.

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  database="studyplay"
)
cursor = db_connection.cursor()
print(db_connection)

def MainDashBoard(request):
    return render(request,'registrationform.html')

def registerform(request):
    if request.method =='POST':
        saverecord=AdminModel()
        saverecord.AdminId=request.POST.get('id')
        saverecord.Pseudo=request.POST.get('name')
        saverecord.Password=request.POST.get('password')
        saverecord.Email=request.POST.get('email')
        saverecord.save()
    return MainDashBoard(request)

def registerFormChild(request):
    if request.method =='POST':
        saverecord=ChildModel()
        """saverecord.ID=request.POST.get('id')"""
        saverecord.Pseudo=request.POST.get("name")
        saverecord.Password=request.POST.get('password')
        saverecord.Email=request.POST.get('email')
        saverecord.save()
    return MainDashBoard(request)
