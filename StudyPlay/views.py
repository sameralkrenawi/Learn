from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from StudyPlay.models import AdminModel
from StudyPlay.models import ChildModel
from StudyPlay.models import WorkersModel
from StudyPlay.models import ParentsModel
from StudyPlay.models import ActivitiesModel
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
    return render(request, 'registrationform.html')

def ChildDash(request):
    return render(request, 'ChildDashBoard/index.html')

def ParentsDash(request):
    return render(request, 'ParentsDashBoard/index.html')

def AdminDash(request):
    return render(request,'AdminDashBoard/index.html')

def index(request):
    return render(request,'index.html')

def registerform(request):
    if request.method =='POST':
        saverecord=AdminModel()
        saverecord.AdminId=request.POST.get('id')
        saverecord.Pseudo=request.POST.get('name')
        #saverecord.Password=request.POST.get('password')
        #
        clearPassNoHash=saverecord.cleaned_data['password']
        password = make_password(clearPassNoHash, None, 'md5')
        saverecord.set_password(password)
        #
        saverecord.Email=request.POST.get('email')
        saverecord.save()
    return MainDashBoard(request)

def registerFormParents(request):
    cursor.execute("SELECT Pseudo,Email FROM parents")
    data = cursor.fetchall()
    cursor.execute("SELECT Pseudo,Email FROM child")
    data2 = cursor.fetchall()

    if request.method =='POST':
        saverecord=ParentsModel()
        """saverecord.ID=request.POST.get('id')"""
        saverecord.Pseudo=request.POST.get("name")
        #saverecord.Password=request.POST.get('password')
        #
        clearPassNoHash=saverecord.cleaned_data['password']
        password = make_password(clearPassNoHash, None, 'md5')
        saverecord.set_password(password)
        #
        saverecord.Email=request.POST.get('email')
        for item in data:
            username,email=item
            if saverecord.Pseudo==username or saverecord.Email==email:
                return ErrorPage(request)
        saverecord.save()
    return MainDashBoard(request)

def registerFormChild(request):
    cursor.execute("SELECT Pseudo,Email FROM child")
    data = cursor.fetchall()
    if request.method =='POST':
        saverecord=ChildModel()
        """saverecord.ID=request.POST.get('id')"""
        saverecord.Pseudo=request.POST.get("name")
        saverecord.Password=request.POST.get('password')
        saverecord.Email=request.POST.get('email')
        for item in data:
            username,email=item
            if saverecord.Pseudo==username or saverecord.Email==email:
                return ErrorPage(request)
        saverecord.save()
    return MainDashBoard(request)

def ErrorPage(request):
    return render(request,'ErrorPage.html')

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
    cursor.execute("SELECT Pseudo,Password FROM Child")
    data2 = cursor.fetchall()
    cursor.execute("SELECT Pseudo,Password FROM Parents")
    data3 = cursor.fetchall()
    if request.method=='POST':
         useridtest=request.POST.get('pseudo')
         passwordtest=request.POST.get('password')
    for item in data:    
        ID,Adminid,Pseudo,Password,type= item
        if useridtest==Pseudo and passwordtest == Password:
             return AdminDash(request)    
    for item in data2:    
        Pseudo,Password= item
        if useridtest==Pseudo and passwordtest == Password:
             return ChildDash(request)      
    for item in data3:    
        Pseudo,Password= item
        if useridtest==Pseudo and passwordtest == Password:
             return ParentsDash(request)    
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
                cursor.execute("DELETE FROM workers WHERE workers.ID = '%s';"%(ID))
                db_connection.commit()
                messages.success(request,'עובד הוסר מהמערכת ')
                return get_workers_table(request)
    else: 
        messages.success(request,'עובד לא נמצא במערכת ')
        return index(request)

def ManageActivities(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM activities")
    data = cursor.fetchall()
    for item in data:
        ID,Name,Subject = item
        result['data'].append({
            'ID':ID,
            'Name':Name,
            'Subject':Subject,
        })
        print(result)
    return render(request,'AdminDashBoard/manageActivities.html', result)

def AddActivity(request):
    cursor.execute("SELECT Name,Subject FROM activities")
    data = cursor.fetchall()
    if request.method =='POST':
        saverecord=ActivitiesModel()
        """saverecord.ID=request.POST.get('id')"""
        saverecord.Name=request.POST.get("name")
        saverecord.Subject=request.POST.get('subject')
        for item in data:
            name,subject=item
            if saverecord.Name==name and saverecord.Subject==subject:
                return ErrorPage(request)
        saverecord.save()
    return ManageActivities(request)

def DeleteActivity(request):
    if request.method=='POST':
        activityID=request.POST.get('id')
        result = []
        cursor.execute("SELECT ID FROM activities")
        data = cursor.fetchall()    
        for item in data:
            ID = item
            if ID == activityID:
                cursor.execute("DELETE FROM activities WHERE ID = '%s';"%(ID))
                db_connection.commit()
                messages.success(request,'Activity was deleted to system')
                return ManageActivities(request)
            else: 
                messages.success(request,'Activity doesnt exist in the system ')
                return ManageActivities(request)



"""def get_ip(request):
    try:
        x_forward=request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward.split(",")[0]
            ip=x_forward.split(",")[0]
        else:
            ip=request.META.get("REMOTE_ADDR")
    except:
        ip=""
    return ip"""