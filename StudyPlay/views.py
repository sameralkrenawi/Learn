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
from StudyPlay.models import ReviewsModel
from StudyPlay.models import ActivityDoneModel
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import mysql.connector
import random

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

def ChildDash(request,userid):
    result={
        'data': []
    }
    cursor.execute("SELECT Pseudo,Password,profile_pic FROM child")
    data = cursor.fetchall()
    if request.method=='POST':
        useridtest=request.POST.get('pseudo')
        passwordtest=request.POST.get('password')
    for item in data:
        Pseudo,Password,profile_pic = item
        if Pseudo==userid:
            result['data'].append({
                'Pseudo':Pseudo,
                'profile_pic':profile_pic,
            })
    print(result)
    return render(request, 'ChildDashBoard/index.html',result)

def WorkerDash(request):
    return render(request,'WorkerDashBoard/index.html')

def contact(request):
    return render(request,'ParentsDashBoard/contact.html')

def ParentsDashReturn(request): 
    return render(request,'login.html')

def InformClient(request):
    return render(request,'AdminDashBoard/sendemail.html')

def ParentsDash(request):
    result={
        'data': []
    }
    cursor.execute("SELECT Pseudo,Password,profile_pic FROM parents")
    data = cursor.fetchall()
    if request.method=='POST':
        useridtest=request.POST.get('pseudo')
        passwordtest=request.POST.get('password')
        for item in data:
            Pseudo,Password,profile_pic = item
            if useridtest==Pseudo and passwordtest == Password:
                result['data'].append({
                    'Pseudo':Pseudo,
                    'profile_pic':profile_pic,
                    })
        print(result)
        return render(request, 'ParentsDashBoard/index.html',result)

def AdminDash(request):
    result={
        'data': []
    }
    cursor.execute("SELECT Pseudo,Password FROM admin")
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
        return render(request, 'AdminDashBoard/index.html',result)

def getGrade(request,userid):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM child")
    data = cursor.fetchall()
    for item in data:
        ID,Pseudo,Password,Age,Email,profile_pic,ParentsPseudo, = item
        if ParentsPseudo==userid:
            result['data'].append({
                'ID':ID,
                'Pseudo':Pseudo,
                'Password':Password,
                'Age':Age,
                'Email':Email,
                'ParentsPseudo':ParentsPseudo,
                'profile_pic':profile_pic,
            })
        print(result)
    #regular registration before 
    #regular registration before 
    return render(request,'ParentsDashBoard/TableChildGrade.html',result) 

def getActivityForChild(request,userid):
    result={
        'data': []
    }
    cursor.execute("SELECT ID,Name FROM activities")
    data = cursor.fetchall()
    for item in data:
        ID,Name= item
        if Name!='Lecture':
            result['data'].append({
                'Name':Name,
            })
    print(result)
    return render(request,'ParentsDashBoard/TableActivitiesGrade.html',result) 

def VideoLibrary(request):
    #regular registration before 
    return render(request,'ChildDashBoard/VideoLibrary.html')    #regular registration before 

def Gradesofchild(request,userid):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM child")
    data = cursor.fetchall()
    for item in data:
        ID,Pseudo,Password,Age,Email,ParentsPseudo,profile_pic = item
        if ParentsPseudo==userid:
            result['data'].append({
                'ID':ID,
                'Pseudo':Pseudo,
                'Password':Password,
                'Age':Age,
                'Email':Email,
                'ParentsPseudo':ParentsPseudo,
                'profile_pic':profile_pic,
            })
        print(result)
    #regular registration before 
    return render(request,'ParentsDashBoard/Gradesofchild.html') 

def ActivityDash(request,userid):
    result={'data': [], 
            'data1' : [],
            'data2' : [] }

    cursor.execute("SELECT * FROM activities")
    data = cursor.fetchall()
    cursor.execute("SELECT Pseudo,profile_pic FROM child")
    data1 = cursor.fetchall()
    cursor.execute("SELECT ID,Name FROM activities")
    data2 = cursor.fetchall()
    for item in data:
        ID,Name,Subject,Link = item
        if Name!='Lecture':
            result['data'].append({
                'ID':ID,
                'Name':Name,
                'Subject':Subject,
                'Link':Link+'/'+userid,
            })
    for item in data1:
        Pseudo,profile_pic=item
        if(Pseudo==userid):
            result['data1'].append({
                'Pseudo':Pseudo,
                'profile_pic':profile_pic,
            })
    for item in data2:
        ID,Name=item
        if Name=='Lecture':
             result['data2'].append({
                'ID':ID,
                'Name':Name,
                'Subject':Subject,
                'Link':Link+'/'+userid,
             })
    print(result)
    return render(request,'ActivityDashBoard/index.html', result)

def ExerciceLecture(request,userid):
    return render(request,'ActivityDashBoard/ExerciceLecture.html')

def ExercicePuzzle(request,userid):
    return render(request,'ActivityDashBoard/ExercicePuzzle.html')

def ExerciseMemory(request,userid):
    return render(request,'ActivityDashBoard/ExerciseMemory.html')    
    
def getActivityDone(request,nameAct,userid):
    result={'data': [], 
            'data1' : [], 
            'data2' : []
            }
    cursor.execute("SELECT ID,Name FROM activities")
    data = cursor.fetchall()
    cursor.execute("SELECT Pseudo,ParentsPseudo FROM child")
    data1 = cursor.fetchall()
    cursor.execute("SELECT ID,PseudoC,NameAct,NumOfGame FROM activitydone")
    data2 = cursor.fetchall()
    cursor.execute("SELECT ID,max(NumOfGame) FROM activitydone WHERE activitydone.NameAct='%s';"%(nameAct))
    data3 = cursor.fetchall()
    for item in data:
        ID,Name = item
        if Name==nameAct:
            result['data'].append({
                'ID':ID,
                'Name':Name,
                'UserID':userid,
            })
    for item in data1:
        Pseudo,ParentsPseudo=item
        if Pseudo==userid:
            result['data1'].append({
                'Pseudo':Pseudo,
                'ParentsPseudo':ParentsPseudo,
                'Grade':random.randint(75,100)
            })
    for item in data3:
        ID,maxN=item

    for item in data2:
        ID,PseudoC,NameAct,NumOfGame=item
        if PseudoC==userid and NameAct==nameAct and NumOfGame==maxN:
            result['data2'].append({
                'ID':ID,
                'NumOfGame':NumOfGame+1,
            })
            break



           
    print(result)
    return render(request,'ActivityDashBoard/getActivityDone.html',result)  
        
def AddGrades(request,userid): 
    if request.method =='POST':
        saverecord=ActivityDoneModel()
        saverecord.NameAct=request.POST.get('Name')
        saverecord.PseudoC=request.POST.get('Pseudo')
        saverecord.PseudoP=request.POST.get('PseudoP')
        saverecord.Grade=request.POST.get('Grade')
        saverecord.NumOfGame=request.POST.get('NumOfGame')
        saverecord.save() 
    return ChildDash(request,userid)

def index(request):
    return render(request,'index.html')

def changepassword(request):
    #page to change password to all users
    return render(request, 'changepassword.html')

def changepseudo(request):
    #page to change password to all users
    return render(request, 'changepseudo.html')

def changepicture(request):
    #page to change password to all users
    return render(request, 'changepicture.html')

def addReviews(request):
    if request.method =='POST':
        saverecord=ReviewsModel()
        saverecord.Description=request.POST.get('description')
        saverecord.Ratings=request.POST.get('ratings')
        saverecord.save()
        messages.success(request,'Review is sended successfuly')
    else:
        return render(request,'ParentsDashBoard/addReviews.html')    
    return ParentsDash(request)

def getReviews(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM reviews")
    data = cursor.fetchall()
    for item in data:
        ID,Description,Ratings = item
        result['data'].append({
            'ID':ID,
            'Description':Description,
            'Ratings':Ratings,
        })
        print(result)
    return render(request,'AdminDashBoard/getReviews.html', result)

def getChildrenInformation(request):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM child")
    data = cursor.fetchall()
    for item in data:
        ID,Pseudo,Password,Age,Email,profile_pic,ParentsPseudo= item
        result['data'].append({
            'ID':ID,
            'Pseudo':Pseudo,
            'Password':Password,
            'Age':Age,
            'Email':Email,
            'profile_pic':profile_pic,
            'ParentsPseudo':ParentsPseudo,
        })
        print(result)
    return render(request,'ParentsDashBoard/getChildrenInformation.html', result)

def registerform(request):
    cursor.execute("SELECT * FROM admin")
    data = cursor.fetchall()
    if request.method =='POST':
        userID=request.POST.get('name')
        userEmail=request.POST.get('email')
        saverecord=AdminModel()
        saverecord.Adminid=request.POST.get('id')
        saverecord.Pseudo=request.POST.get('name')
        saverecord.Password=request.POST.get('password')
        saverecord.Email=request.POST.get('email')
        for item in data:
            ID,adminID,username,password,email=item
            if userID==username or userEmail==email:
                return ErrorPage(request)
        saverecord.save()
        messages.success(request,'Register Success ')   
    return MainDashBoard(request)

def registerFormParents(request):    
    cursor.execute("SELECT * FROM Parents")
    data = cursor.fetchall()       
    if request.method =='POST':
        userID=request.POST.get('name')
        userEmail=request.POST.get('email')
        saverecord=ParentsModel()
        saverecord.Pseudo=request.POST.get('name')
        saverecord.Password=request.POST.get('password')  
        saverecord.Email=request.POST.get('email')
        saverecord.country=request.POST.get('country')
        saverecord.profile_pic="profile1.png"
        for item in data:
            id,username,password,email,country,profile_pic=item
            if userID==username and userEmail==email:
                return ErrorPage(request)
        saverecord.save()
    return MainDashBoard(request)

def registerFormChild(request):
    cursor.execute("SELECT * FROM child")
    data = cursor.fetchall()
    if request.method =='POST':
        userID=request.POST.get('name')
        userEmail=request.POST.get('email')
        saverecord=ChildModel()
        saverecord.Pseudo=request.POST.get("name")
        saverecord.Password=request.POST.get('password')
        saverecord.Age=request.POST.get("age")
        saverecord.Email=request.POST.get('email')
        saverecord.profile_pic="profile1.png"
        saverecord.ParentsPseudo=request.POST.get('pseudo')
        for item in data:
            username,password,age,email,profile_pic,ParentsPseudo=item
            if userID==username or userEmail==email:
                return ErrorPage(request)
        saverecord.save()
    return MainDashBoard(request)

def ErrorPage(request):
    return render(request,'ErrorPage.html')

def after_approuval_worker_insert(request):
    cursor.execute("SELECT * FROM workers")
    data = cursor.fetchall()
    if request.method=='POST':
        userID=request.POST.get('name')
        userEmail=request.POST.get('email')
        saverecord=WorkersModel()
        saverecord.Workerid=request.POST.get('id')
        saverecord.Pseudo=request.POST.get('name')
        saverecord.Password=request.POST.get('password')
        saverecord.Email=request.POST.get('email')
        saverecord.type=request.POST.get('type')
        for item in data:
            id,workerid,username,password,email,type=item
            if userID==username or userEmail==email:
                return ErrorPage(request)
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
		 ['studyplaycontact@gmail.com'], 
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
		 ['studyplaycontact@gmail.com'], 
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
        ID,Pseudo,Password,Age,Email,profile_pic,ParentsPseudo = item
        result['data'].append({
            'ID':ID,
            'Pseudo':Pseudo,
            'Password':Password,
            'Age':Age,
            'Email':Email,
            'profile_pic':profile_pic,
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
        ID,Pseudo,Password,Email,country,profile_pic = item
        result['data'].append({
            'id':ID,
            'Pseudo':Pseudo,
            'Password':Password,
            'Email':Email,
            'country':country,
            'profile_pic':profile_pic,
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
             return ChildDash(request,userid)    
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
        ID,Name,Subject,Link = item
        result['data'].append({
            'ID':ID,
            'Name':Name,
            'Subject':Subject,
            'Link':Link,
        })
        print(result)
    return render(request,'AdminDashBoard/manageActivities.html', result)

def AddActivity(request):
    cursor.execute("SELECT Name,Subject FROM activities")
    data = cursor.fetchall()
    if request.method =='POST':
        saverecord=ActivitiesModel()
        """saverecord.ID=request.POST.get('id')"""
        saverecord.Name=request.POST.get('name')
        saverecord.Subject=request.POST.get('subject')
        saverecord.Link='/StudyPlay/Ex'+request.POST.get('name')
        for item in data:
            name,subject=item
            if saverecord.Name==name and saverecord.Subject==subject:
                return ErrorPage(request)
        saverecord.save()
        return ManageActivities(request)

def DeleteActivity(request):
    if request.method=='POST':
        activityIDs=request.POST.get('id')
        activityID=int(activityIDs)
        activityName=request.POST.get('name')
        result = []
        cursor.execute("SELECT ID,Name FROM activities")
        data = cursor.fetchall()    
        for item in data:
            ID,Name = item
            if ID == activityID and Name==activityName:
                cursor.execute("DELETE FROM activities WHERE activities.ID = '%s';"%(ID))
                db_connection.commit()
                messages.success(request,'Activity was deleted to system')
                return ManageActivities(request)
        messages.success(request,'Activity doesnt exist in the system ')
        return AdminDash(request)

def after_approuval_child_insert(request):
    cursor.execute("SELECT * FROM child")
    data = cursor.fetchall()  
    if request.method=='POST':
        userPseudo=request.POST.get('pseudo')
        userPseudoP=request.POST.get('pseudoP')
        saverecord=ChildModel()
        saverecord.Pseudo=request.POST.get('pseudo')
        saverecord.Password=request.POST.get('password')
        saverecord.Age=request.POST.get('age')
        saverecord.Email=request.POST.get('email')
        saverecord.profile_pic="profile1.png"
        saverecord.ParentsPseudo=request.POST.get('pseudoP')
        for item in data:
            id,pseudo,password,age,email,profile_pic,pseudoP=item
            if userPseudoP==pseudoP:
                if userPseudo==pseudo:
                    return ErrorPage(request)
        saverecord.save()
        messages.success(request,'Child Add ')
        send_mail('Contact Form',
		         'child add', 
		         settings.EMAIL_HOST_USER,
		         ['studyplaycontact@gmail.com'], 
		        fail_silently=False)	
        return get_new_child_table(request,request.POST.get('pseudo'))    
    messages.success(request,'Cant Add child')
    return ParentsDash(request)            

def get_new_child_table(request,userid):
    result={
        'data': []
    }
    cursor.execute("SELECT * FROM child")
    data = cursor.fetchall()
    for item in data:
        ID,Pseudo,Password,Age,Email,profile_pic,ParentsPseudo = item
        if ParentsPseudo==userid:
            result['data'].append({
                'ID':ID,
                'Pseudo':Pseudo,
                'Password':Password,
                'Age':Age,
                'Email':Email,
                'profile_pic':profile_pic,
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
        ID,Pseudo,Password,Age,Email,ParentsPseudo,profile_pic = item
        if ParentsPseudo==userid:
            result['data'].append({
                'ID':ID,
                'Pseudo':Pseudo,
                'Password':Password,
                'Age':Age,
                'Email':Email,
                'ParentsPseudo':ParentsPseudo,
                'profile_pic':profile_pic,
               
            })
     
                    
        print(result)
    return render(request,'ParentsDashBoard/deletechild.html', result)

def Deletechild(request):
    if request.method=='POST':
        childPseudo=request.POST.get('pseudo')
        result = []
        cursor.execute("SELECT * FROM child")
        data = cursor.fetchall()    
        for item in data:
            ID,Pseudo,Password,Age,Email,Link,ParentsPseudo= item
            if (Pseudo == childPseudo):
                cursor.execute("DELETE FROM child WHERE child.ID = '%s';"%(ID))
                db_connection.commit()
                messages.success(request,'Child Delete ')
                send_mail('Contact Form',
		         'child delete', 
		         settings.EMAIL_HOST_USER,
		         ['studyplaycontact@gmail.com'], 
		         fail_silently=False)	
                return get_child_table(request,ParentsPseudo) 
        messages.success(request,'Child Not find enter the details again ')
        return ParentsDash(request)

def CHANGE_PICTURE(request):
    if request.method=='POST':
        useridtest=request.POST.get('pseudo')
        passwordcurrentpassword=request.POST.get('current_password')
        passwordtest=request.POST.get('password')
        cursor.execute("SELECT Pseudo,Password,profile_pic FROM Parents")
        data = cursor.fetchall()    
        flag=0
        for item in data:
            Pseudo,Password,profile_pic = item
            if  Pseudo==useridtest and Password == passwordcurrentpassword :
                cursor.execute("UPDATE `Parents` SET `profile_pic` = '%s' WHERE `Parents`.`Pseudo` = '%s';"%(passwordtest,useridtest))
                db_connection.commit()
                messages.success(request,'Picture Change')
                return registration(request)  
        cursor.execute("SELECT Pseudo,Password,profile_pic FROM child")
        data = cursor.fetchall()    
        for item in data:
            Pseudo,Password,profile_pic = item
            if Pseudo==useridtest and Password == passwordcurrentpassword :
                cursor.execute("UPDATE `child` SET `profile_pic` = '%s' WHERE `child`.`Pseudo` = '%s';"%(passwordtest,useridtest))
                db_connection.commit()
                messages.success(request,'Picture Change')
                return registration(request)  
        cursor.execute("SELECT Pseudo,Password,profile_pic FROM workers")
        data = cursor.fetchall()    
        for item in data:
            Pseudo,Password,profile_pic = item
            if Pseudo==useridtest and Password == passwordcurrentpassword :
                cursor.execute("UPDATE `workers` SET `profile_pic` = '%s' WHERE `workers`.`Pseudo` = '%s';"%(passwordtest,useridtest))
                db_connection.commit()
                messages.success(request,'Picture Change')
                return registration(request)  
        messages.error(request,'! הפרט ים שהוזנו לא נמצאים במערכת')   
        return changepassword(request)

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

def CHANGE_PSEUDO(request):
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
                cursor.execute("UPDATE `Parents` SET `Pseudo` = '%s' WHERE `Parents`.`Pseudo` = '%s';"%(passwordtest,useridtest))
                db_connection.commit()
                messages.success(request,'Pseudo Change')
                return registration(request)  
        cursor.execute("SELECT Pseudo,Password FROM child")
        data = cursor.fetchall()    
        for item in data:
            Pseudo,Password = item
            if Pseudo==useridtest and Password == passwordcurrentpassword :
                cursor.execute("UPDATE `child` SET `Pseudo` = '%s' WHERE `child`.`Pseudo` = '%s';"%(passwordtest,useridtest))
                db_connection.commit()
                messages.success(request,'Pseudo Change')
                return registration(request)  
        cursor.execute("SELECT Pseudo,Password FROM workers")
        data = cursor.fetchall()    
        for item in data:
            Pseudo,Password = item
            if Pseudo==useridtest and Password == passwordcurrentpassword :
                cursor.execute("UPDATE `workers` SET `Pseudo` = '%s' WHERE `workers`.`Pseudo` = '%s';"%(passwordtest,useridtest))
                db_connection.commit()
                messages.success(request,'Pseudo Change')
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
        ID,Pseudo,Password,Age,Email,profile_pic,ParentsPseudo = item
        if ParentsPseudo==userid:
            result['data'].append({
                'ID':ID,
                'Pseudo':Pseudo,
                'Password':Password,
                'Age':Age,
                'Email':Email,
                'profile_pic':profile_pic,
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

def send_notification(request):

    """client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    if request.method == 'POST':
        user_whatsapp_number = request.POST['user_number']
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Your {} order of {} has shipped and should be delivered on {}. Details: {}'.format(
                order_details['amount'], order_details['item'], order_details['date_of_delivery'],
                order_details['address']),
            to='whatsapp:+{}'.format(user_whatsapp_number)
        )
        print(user_whatsapp_number)
        print(message.sid)
        return HttpResponse('Great! Expect a message...')"""
    return render(request, 'phone.html')

def Statistics(request):
    labels = []
    data = []
    queryset_labels = ActivityDoneModel.objects.values('NumOfGame')
    queryset_data = ActivityDoneModel.objects.values('Grade')
    for entry in queryset_labels:
        labels.append(entry['NameAct'])
    for entry in queryset_data:
        data.append(entry['Grade'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
