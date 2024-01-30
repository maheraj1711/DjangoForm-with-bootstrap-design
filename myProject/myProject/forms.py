from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myApp.models import*


class SignupForm(UserCreationForm):
    
    USER_TYPE_CHOICES = (
    ('admin', 'Admin'),
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ('employee', 'Employee'),
    ('stuff', 'Stuff'),
    ('nurse', 'Nurse'),
    
)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label='User Type')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
            'user_type': 'User Type',
        }

            
class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    


class studentForm(forms.ModelForm):

    class Meta:
        model=studentModel
        fields=['firstname','username','department','city']
        labels={
            'firstname':'Enter Your Firstname',
            'username':'Enter Your Username',
            'department':'Enter Your Department',
            'city':'Enter Your City',
        }



class teacherForm(forms.ModelForm):

    class Meta:
        model=teacherModel
        fields=['firstname','username','department','city']
        labels={
            'firstname':'Enter Your Firstname',
            'username':'Enter Your Username',
            'department':'Enter Your Department',
            'city':'Enter Your City',
        }


class employeeForm(forms.ModelForm):

    class Meta:
        model=employeeModel
        fields=['firstname','username','department','city']
        labels={
            'firstname':'Enter Your Firstname',
            'username':'Enter Your Username',
            'department':'Enter Your Department',
            'city':'Enter Your City',
        }
        
        

class StuffForm(forms.ModelForm):

    class Meta:
        model=StuffModel
        fields=['firstname','username','department','city']
        labels={
            'firstname':'Enter Your Firstname',
            'username':'Enter Your Username',
            'department':'Enter Your Department',
            'city':'Enter Your City',
        }
        

class NurseForm(forms.ModelForm):

    class Meta:
        model=NurseModel
        fields=['firstname','username','department','city']
        labels={
            'firstname':'Enter Your Firstname',
            'username':'Enter Your Username',
            'department':'Enter Your Department',
            'city':'Enter Your City',
        }                