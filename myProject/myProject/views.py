from django.shortcuts import render, redirect
from myApp.models import *
from myProject.forms import*
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required

from .forms import SignupForm


def user_signup(request):
    if request.method == 'POST':
        form =SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form =SignupForm()

    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('myDashboard')
            elif user:
                login(request, user)
                return redirect('studentHome')
            elif user:
                login(request, user)
                return redirect('teacherHome')
            elif user:
                login(request, user)
                return redirect('employeeHome')
            elif user:
                login(request, user)
                return redirect('Stuff')
            elif user:
                login(request, user)
                return redirect('NurseHome')
                  
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')



@login_required
def myDashboard(request):


    return render(request, 'dashboard.html')


def studentHome(request):

    student=studentModel.objects.all()

    form=studentForm()

    context={
        'student':student,
        'form':form
    }


    return render(request, 'studentHome.html', context)


def studentAdd(request):

    if request.method=='POST':

        form=studentForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect("studentHome")
        

def studentDelete(request,myid):
    student=studentModel.objects.get(id=myid)
    student.delete()
    
    return redirect("studentHome") 


def studentUpdate(request, myid):
    student=studentModel.objects.get(id=myid)
    form=studentForm(instance=student)

    if request.method=='POST':
        form=studentForm(request.POST, instance=student)
        form.save()
        return redirect("studentHome")

    return render(request,'studentUpdate.html',{'form':form})






def teacherHome(request):

    teacher=teacherModel.objects.all()

    form=teacherForm()

    context={
        'teacher':teacher,
        'form':form
    }


    return render(request, 'teacherHome.html', context)


def teacherAdd(request):

    if request.method=='POST':

        form=teacherForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect("teacherHome")
        
def teacherDelete(request,myid):
    teacher=teacherModel.objects.get(id=myid)
    teacher.delete()
    
    return redirect("teacherHome") 


def teacherUpdate(request, myid):
    teacher=teacherModel.objects.get(id=myid)
    form=teacherForm(instance=teacher)

    if request.method=='POST':
        form=teacherForm(request.POST, instance=teacher)
        form.save()
        return redirect("teacherHome")

    return render(request,'teacherUpdate.html',{'form':form})





def employeeHome(request):

    employee=employeeModel.objects.all()

    form=employeeForm()

    context={
        'employee':employee,
        'form':form
    }
    return render(request, 'employeeHome.html', context)


def employeeAdd(request):

    if request.method=='POST':

        form=employeeForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect("employeeHome")
        
def employeeDelete(request,myid):
    employee=employeeModel.objects.get(id=myid)
    employee.delete()
    
    return redirect("employeeHome") 


def employeeUpdate(request, myid):
    employee=employeeModel.objects.get(id=myid)
    form=employeeForm(instance=employee)

    if request.method=='POST':
        form=employeeForm(request.POST, instance=employee)
        form.save()
        return redirect("employeeHome")

    return render(request,'employeeUpdate.html',{'form':form})

def Stuff(request):

    Stuff=StuffModel.objects.all()

    form=StuffForm()

    context={
        'Stuff':Stuff,
        'form':form
    }
    return render(request, 'StuffHome.html', context)


def Stuffadd(request):

    if request.method=='POST':

        form=StuffForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect("Stuff")
        
def StuffDelete(request,myid):
    Stuff=StuffModel.objects.get(id=myid)
    Stuff.delete()
    
    return redirect("Stuff") 


def StuffUpdate(request, myid):
    Stuff=StuffModel.objects.get(id=myid)
    form=StuffForm(instance=Stuff)

    if request.method=='POST':
        form=StuffForm(request.POST, instance=Stuff)
        form.save()
        return redirect("Stuff")

    return render(request,'StuffUpdate.html',{'form':form})

def NurseHome(request):

    Nurse=NurseModel.objects.all()

    form=NurseForm()

    context={
        'Nurse':Nurse,
        'form':form
    }
    return render(request, 'NurseHome.html', context)


def NurseAdd(request):

    if request.method=='POST':

        form=NurseForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect("NurseHome")
        
def NurseDelete(request,myid):
    Nurse=NurseModel.objects.get(id=myid)
    Nurse.delete()
    
    return redirect("NurseHome") 


def NurseUpdate(request, myid):
    Nurse=NurseModel.objects.get(id=myid)
    form=NurseForm(instance=Nurse)

    if request.method=='POST':
        form=NurseForm(request.POST, instance=Nurse)
        form.save()
        return redirect("NurseHome")

    return render(request,'NurseUpdate.html',{'form':form})