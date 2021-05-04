from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from StudyPlay.models import AdminModel
from StudyPlay.models import ChildModel
from StudyPlay.models import WorkersModel
from StudyPlay.models import ParentsModel
from StudyPlay.models import ActivitiesModel
from StudyPlay.models import CountriesModel
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

import mysql.connector
# Create your views here.
global userid 

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="studyplay"
)
cursor = db_connection.cursor()
print(db_connection)

def registration(request):
    #regular registration before 
    return render(request,'registrationform.html')    #regular registration before 

def MainDashBoard(request):
    return render(request, 'registrationform.html')

def ChildDash(request):
    return render(request, 'ChildDashBoard/index.html')

def WorkerDash(request):
    return render(request,'WorkerDashBoard/index.html')

def contact(request):
    return render(request,'AdminDashBoard/contact.html')

def InformClient(request):
    return render(request,'AdminDashBoard/sendemail.html')

def ParentsDash(request):
    result={
        'data': []
    }
    cursor.execute("SELECT Pseudo,Password FROM parents")
    data = cursor.fetchall()
    if request.method=='POST':
        useridtest=request.POST.get('pseudo')
        passwordtest=request.POST.get('password')
        for item in data:
            Pseudo,Password = item
            if useridtest==Pseudo and passwordtest == Password:
                result['data'].append({
                    'Pseudo':Pseudo,
                    })
        print(result)
        return render(request, 'ParentsDashBoard/index.html',result)

def AdminDash(request):
    return render(request,'AdminDashBoard/index.html')

def ActivityDash(request):
    return render(request,'ChildDashBoard/ActivityDash.html')  

def ExerciceLecture(request):
    return render(request,'ChildDashBoard/ExerciceLecture.html')

def ExercicePuzzle(request):
    return render(request,'ChildDashBoard/ExercicePuzzle.html')

def index(request):
    return render(request,'index.html')

def changepassword(request):
    #page to change password to all users
    return render(request, 'changepassword.html')

def registerform(request):
    if request.method =='POST':
        saverecord=AdminModel()
        saverecord.AdminId=request.POST.get('id')
        saverecord.Pseudo=request.POST.get('name')
        saverecord.Password=request.POST.get('password')
        saverecord.Email=request.POST.get('email')
        saverecord.save()
        messages.success(request,'Register Success ')
    else:
        return registerFormParents(request)    
    return MainDashBoard(request)

def registerFormParents(request):    
    cursor.execute("SELECT * FROM Parents")
    data = cursor.fetchall()       
    if request.method =='POST':
        saverecord=ParentsModel()
        saverecord.Pseudo=request.POST.get("name")
        saverecord.Password=request.POST.get('password')  
        saverecord.Email=request.POST.get('email')
        saverecord.country=request.POST.get('country')
        for item in data:
            id,username,password,email=item
            if saverecord.Pseudo==username or saverecord.Email==email:
                return ErrorPage(request)
        saverecord.save()
    return MainDashBoard(request)

def registerFormChild(request):
    cursor.execute("SELECT FROM child")
    data = cursor.fetchall()
    if request.method =='POST':
        saverecord=ChildModel()
        saverecord.Pseudo=request.POST.get("name")
        saverecord.Password=request.POST.get('password')
        saverecord.Age=request.POST.get("age")
        saverecord.Email=request.POST.get('email')
        saverecord.ParentsPseudo=request.POST.get('pseudo')
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
        messages.success(request,'Worker Add ')
    else:
        messages.success(request,'Cant Add Worker ')
        return AdminDash(request)    
    return get_new_workers_table(request)          

def sendemail(request):
    if request.method == 'POST':
        message = request.POST['message']
        send_mail('Contact Form',
		 message, 
		 settings.EMAIL_HOST_USER,
		 ['david.teboul.95@gmail.com'], 
		 fail_silently=False)	
    return render(request, 'AdminDashBoard/contact.html')

def indexLibrary(request):
    #regular registration before 
    return render(request,'ParentsDashBoard/indexLibrary.html')    #regular registration before 

def sendWhatss(request):
    if request.method == 'POST':
        message = request.POST['message']
        send_mail('Contact Form',
		 message, 
		 settings.EMAIL_HOST_USER,
		 ['david.teboul.95@gmail.com'], 
		 fail_silently=False)	
    return render(request, 'AdminDashBoard/contact.html')

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

def get_child_FromP_table(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM child")
    data = cursor.fetchall()
    for item in data:
        ID,Pseudo,Password,Age,Email,ParentsPseudo = item
        result['data'].append({
            'ID':ID,
            'Pseudo':Pseudo,
            'Password':Password,
            'Age':Age,
            'Email':Email,
            'ParentsPseudo':ParentsPseudo,
            })
    return render(request,'AdminDashBoard/getchild.html', result)

def get_parents_table(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM Parents")
    data = cursor.fetchall()
    for item in data:
        ID,Pseudo,Password,Email = item
        result['data'].append({
            'id':ID,
            'Pseudo':Pseudo,
            'Password':Password,
            'Email':Email,
        })
    return render(request,'AdminDashBoard/getparents.html', result)

def login(request):  
    cursor.execute("SELECT * FROM admin")
    data = cursor.fetchall()
    if request.method=='POST':
         useridtest=request.POST.get('pseudo')
         passwordtest=request.POST.get('password')
         userid=useridtest
    for item in data:    
        ID,Adminid,Pseudo,Password,type= item
        if useridtest==Pseudo and passwordtest == Password:
             return AdminDash(request)    
    cursor.execute("SELECT Pseudo,Password FROM Child")
    data = cursor.fetchall()
    for item in data:    
        Pseudo,Password= item
        if useridtest==Pseudo and passwordtest == Password:
             return ChildDash(request)    
    cursor.execute("SELECT Pseudo,Password FROM Parents")
    data = cursor.fetchall()
    for item in data:    
        Pseudo,Password= item
        if useridtest==Pseudo and passwordtest == Password:
             return ParentsDash(request) 
    cursor.execute("SELECT Pseudo,Password FROM Workers")
    data = cursor.fetchall()
    for item in data:    
        Pseudo,Password= item
        if useridtest==Pseudo and passwordtest == Password:
            return WorkerDash(request)        
    else :
        messages.error(request,' הפרטים שהוזנו לא נמצאים במערכת נא לחכות לאישור אם הפרטים נכונים')   
        return registration(request)    

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

def after_approuval_child_insert(request):
    if request.method=='POST':
        saverecord=ChildModel()
        saverecord.Pseudo=request.POST.get('name')
        saverecord.Password=request.POST.get('password')
        saverecord.Age=request.POST.get('age')
        saverecord.Email=request.POST.get('email')
        saverecord.ParentsPseudo=request.POST.get('pseudo')
        saverecord.save()
        messages.success(request,'Child Add ')
        send_mail('Contact Form',
		         'child add', 
		         settings.EMAIL_HOST_USER,
		         ['david.teboul.95@gmail.com'], 
		        fail_silently=False)	
    else:
        messages.success(request,'Cant Add child')
        return ParentsDash(request)    
    return get_new_child_table(request,request.POST.get('pseudo'))          

def get_new_child_table(request,userid):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM child")
    data = cursor.fetchall()
    for item in data:
        ID,Pseudo,Password,Age,Email,ParentsPseudo = item
        if ParentsPseudo==userid:
            result['data'].append({
                'ID':ID,
                'Pseudo':Pseudo,
                'Password':Password,
                'Age':Age,
                'Email':Email,
                'ParentsPseudo':ParentsPseudo,
            })
        print(result)
    return render(request,'ParentsDashBoard/addchild.html', result)

def get_child_table(request,userid):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM child")
    data = cursor.fetchall()
    for item in data:
        ID,Pseudo,Password,Age,Email,ParentsPseudo = item
        if ParentsPseudo==userid:
            result['data'].append({
                'ID':ID,
                'Pseudo':Pseudo,
                'Password':Password,
                'Age':Age,
                'Email':Email,
                'ParentsPseudo':ParentsPseudo,
            })
        print(result)
    return render(request,'ParentsDashBoard/deletechild.html', result)

def Deletechild(request):
    if request.method=='POST':
        childname=request.POST.get('name')
        Parentname=request.POST.get('pseudo')
        result = []
        cursor.execute("SELECT * FROM child")
        data = cursor.fetchall()    
        for item in data:
            ID,Pseudo,Password,Age,Email,ParentsPseudo= item
            if (Pseudo == childname and Parentname == ParentsPseudo)  :
                cursor.execute("DELETE FROM child WHERE child.ID = '%s';"%(ID))
                db_connection.commit()
                messages.success(request,'Child Delete ')
                send_mail('Contact Form',
		         'child delete', 
		         settings.EMAIL_HOST_USER,
		         ['david.teboul.95@gmail.com'], 
		         fail_silently=False)	
                return get_child_table(request,ParentsPseudo)
    else: 
        messages.success(request,'Child Not find enter the details againe ')
        return index(request)

def CHANGE_PASSWORD(request):
    if request.method=='POST':
        useridtest=request.POST.get('pseudo')
        passwordcurrentpassword=request.POST.get('current_password')
        passwordtest=request.POST.get('password')
        cursor.execute("SELECT Pseudo,Password FROM Parents")
        data = cursor.fetchall()    
        flag=0
        for item in data:
            Pseudo,Password = item
            if  Pseudo==useridtest and Password == passwordcurrentpassword :
                cursor.execute("UPDATE `Parents` SET `Password` = '%s' WHERE `Parents`.`Pseudo` = '%s';"%(passwordtest,useridtest))
                db_connection.commit()
                messages.success(request,'סיסמא הוחלפה בהצלחה')
                return registration(request)  
        cursor.execute("SELECT Pseudo,Password FROM child")
        data = cursor.fetchall()    
        for item in data:
            Pseudo,Password = item
            if Pseudo==useridtest and Password == passwordcurrentpassword :
                cursor.execute("UPDATE `child` SET `Password` = '%s' WHERE `child`.`Pseudo` = '%s';"%(passwordtest,useridtest))
                db_connection.commit()
                messages.success(request,'סיסמא הוחלפה בהצלחה')
                return registration(request)  
        cursor.execute("SELECT Pseudo,Password FROM workers")
        data = cursor.fetchall()    
        for item in data:
            Pseudo,Password = item
            if Pseudo==useridtest and Password == passwordcurrentpassword :
                cursor.execute("UPDATE `workers` SET `Password` = '%s' WHERE `workers`.`Pseudo` = '%s';"%(passwordtest,useridtest))
                db_connection.commit()
                messages.success(request,'סיסמא הוחלפה בהצלחה')
                return registration(request)  
        messages.error(request,'! הפרט ים שהוזנו לא נמצאים במערכת')   
        return changepassword(request)

def connect_From_P(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM child")
    data = cursor.fetchall()
    for item in data:
        ID,Pseudo,Password,Age,Email,ParentsPseudo = item
        if ParentsPseudo==request.POST.get('pseudo'):
            ['data'].append({
                'ID':ID,
                'Pseudo':Pseudo,
                'Password':Password,
                'Age':Age,
                'Email':Email,
                'ParentsPseudo':ParentsPseudo,
            })
        print(result)
    return render(request,'ParentsDashBoard/deletechild.html', result)

def get_child_connection(request,userid):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM child")
    data = cursor.fetchall()
    for item in data:
        ID,Pseudo,Password,Age,Email,ParentsPseudo = item
        if ParentsPseudo==userid:
            result['data'].append({
                'ID':ID,
                'Pseudo':Pseudo,
                'Password':Password,
                'Age':Age,
                'Email':Email,
                'ParentsPseudo':ParentsPseudo,
            })
        print(result)
    return render(request,'ParentsDashBoard/ChildConnection.html',result)

def pie_chart(request):
    labels = []
    data = []

    queryset = CountriesModel.objects.order_by('-Count')[:5]
    for country in queryset:
        labels.append(country.Name)
        data.append(country.Count)

    return render(request, 'AdminDashBoard/pie_chart.html', {
        'labels': labels,
        'data': data,
    })


