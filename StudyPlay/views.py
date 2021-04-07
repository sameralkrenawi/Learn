from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from StudyPlay.models import AdminModel
from StudyPlay.models import ChildModel
from StudyPlay.models import WorkersModel
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
<<<<<<< HEAD
    cursor.execute("SELECT Pseudo,Email FROM Child")
    data = cursor.fetchall()
=======
>>>>>>> 2467cf06e43bed0eff31b9117570059c85e88125
    if request.method =='POST':
        saverecord=ChildModel()
        """saverecord.ID=request.POST.get('id')"""
        saverecord.Pseudo=request.POST.get("name")
        saverecord.Password=request.POST.get('password')
        saverecord.Email=request.POST.get('email')
<<<<<<< HEAD
        for item in data:
            username,email=item
            if saverecord.Pseudo==username or saverecord.Email==email:
                return ErrorPage(request)
=======
>>>>>>> 2467cf06e43bed0eff31b9117570059c85e88125
        saverecord.save()
    return MainDashBoard(request)

def after_approuval_worker_insert(request):
    if request.method=='POST':
        saverecord=WorkersModel()
        saverecord.Workerid=request.POST.get('id')
        saverecord.Pseudo=request.POST.get('name')
        saverecord.Password=request.POST.get('password')
        saverecord.Email=request.POST.get('email')
        saverecord.type=request.POST.get('type')
        saverecord.save()
    return get_new_workers_table(request)          


def get_new_workers_table(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM workers")
    data = cursor.fetchall()
    for item in data:
        ID,Workerid,Pseudo,Password,Email,type = item
        result['data'].append({
            'id':ID,
            'Workerid':Workerid,
            'Pseudo':Pseudo,
            'Password':Password,
            'Email':Email,
            'type':type,
        })
        print(result)
    return render(request,'AdminDashBoard/addworker.html', result)

def get_workers_table(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM workers")
    data = cursor.fetchall()
    for item in data:
        ID,Workerid,Pseudo,Password,Email,type = item
        result['data'].append({
            'id':ID,
            'Workerid':Workerid,
            'Pseudo':Pseudo,
            'Password':Password,
            'Email':Email,
            'type':type,
        })
        print(result)
    return render(request,'AdminDashBoard/deleteuser.html', result)


def login(request):
    result = []
    cursor.execute("SELECT * FROM admin")
    data = cursor.fetchall()
    if request.method=='POST':
         useridtest=request.POST.get('pseudo')
         passwordtest=request.POST.get('password')
    for item in data:    
        ID,Adminid,Pseudo,Password,type= item
        if useridtest==Pseudo and passwordtest == Password:
             return AdminDash(request)
    return AdminDash(request)


def Deleteworker(request):
    if request.method=='POST':
        useridworker=request.POST.get('id')
        workername=request.POST.get('name')
        result = []
        cursor.execute("SELECT * FROM workers")
        data = cursor.fetchall()    
        for item in data:
            ID,Workerid,Pseudo,Password,Email,type = item
            if Workerid==useridworker and Pseudo == workername :
                cursor.execute("DELETE FROM `workers` WHERE `workers`.`ID` = '%s';"%(ID))
                db_connection.commit()
                messages.success(request,'עובד הוסר מהמערכת ')
                return get_workers_table(request)
    else: 
        messages.success(request,'עובד לא נמצא במערכת ')
        return index(request)


def AdminDash(request):
       return render(request,'index.html')

def index(request):
    return render(request,'index.html')
