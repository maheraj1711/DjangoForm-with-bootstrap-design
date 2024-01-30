from django.db import models
   
class studentModel(models.Model):


    firstname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname
    

class teacherModel(models.Model):


    firstname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname
    

class employeeModel(models.Model):


    firstname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname
    
class StuffModel(models.Model):


    firstname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname  
    
    
class NurseModel(models.Model):


    firstname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.firstname      