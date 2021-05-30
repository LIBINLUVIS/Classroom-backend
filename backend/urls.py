from knox import views as knox_views
from .views import RegisterAPI,LoginAPI
from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('users',views.users,name="users"),
    path('create-class/', views.CreateClass, name="create-class"),
	path('classes/', views.classes, name="classes"),
    path('create-class/<int:pk>/', views.classview, name="createView"),
    path('userinfo/', views.userinfo, name="userinfo"),
    path('user-class/', views.userclass, name="userinfo"),
    path('Works/<int:pk>/',views.Works,name="Works"),
    path('Addworks/<int:pk>/',views.Addworks,name="Addworks"),
    path('Submitwork/<int:pk>/',views.Submitwork,name="Submitwork"),
    path('StudentWork/<int:pk>/',views.StudentWork,name="StudentWork"),
    path('getresponses/<int:pk>/',views.getresponses,name='getresponse'),
    path('editclass/<int:pk>/',views.updateclass,name='updateclass'),
    path('Joinclass/<int:pk>/',views.Joinclass,name='joinclass'),
    path('getjoinclass',views.getJoinclass,name='getjoinclass'),  #make a / after url if not working
    path('submitstatus/',views.submitstatus,name='submitstatus')
   
   
]



