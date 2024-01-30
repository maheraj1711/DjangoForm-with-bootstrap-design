
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myProject.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('myDashboard', myDashboard, name='myDashboard'),
    path('studentHome', studentHome, name='studentHome'),
    path('studentAdd', studentAdd, name='studentAdd'),
    path('studentDelete/<str:myid>', studentDelete, name='studentDelete'),
    path('studentUpdate/<str:myid>', studentUpdate, name='studentUpdate'),


    path('teacherHome', teacherHome, name='teacherHome'),
    path('teacherAdd', teacherAdd, name='teacherAdd'),
    path('teacherDelete/<str:myid>', teacherDelete, name='teacherDelete'),
    path('teacherUpdate/<str:myid>', teacherUpdate, name='teacherUpdate'),


    path('employeeHome', employeeHome, name='employeeHome'),
    path('employeeAdd', employeeAdd, name='employeeAdd'),
    path('employeeDelete/<str:myid>', employeeDelete, name='employeeDelete'),
    path('employeeUpdate/<str:myid>', employeeUpdate, name='employeeUpdate'),
    
    path('Stuff', Stuff, name='Stuff'),
    path('Stuffadd', Stuffadd, name='Stuffadd'),
    path('StuffDelete/<str:myid>', StuffDelete, name='StuffDelete'),
    path('StuffUpdate/<str:myid>', StuffUpdate, name='StuffUpdate'),
    
    path('NurseHome', NurseHome, name='NurseHome'),
    path('NurseAdd', NurseAdd, name='NurseAdd'),
    path('NurseDelete/<str:myid>', NurseDelete, name='NurseDelete'),
    path('NurseUpdate/<str:myid>', NurseUpdate, name='NurseUpdate'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
