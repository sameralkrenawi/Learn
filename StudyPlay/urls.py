from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('Test', views.MainDashBoard, name='main'),
    path('registerform', views.registerform) ,
    path('registerformchild', views.registerFormChild) ,
    path('registerformparents', views.registerFormParents) ,
    path('ErrorPage',views.ErrorPage,name="ErrorPage"),
    path('index', views.index, name='index'),
    path('after_approuval_worker_insert', views.after_approuval_worker_insert),
    path('get_new_workers_table', views.get_new_workers_table),
    path('login', views.login),
    path('Deleteworker', views.Deleteworker),
    path('get_workers_table', views.get_workers_table),
    path('get_new_workers_table', views.get_new_workers_table),
    path('adminDash', views.AdminDash),
    path('childDash', views.ChildDash),
    path('parentDash', views.ParentsDash),
    path('manageActivities', views.ManageActivities),
    path('addActivity', views.AddActivity),
    path('deleteActivity', views.DeleteActivity),
    ]
