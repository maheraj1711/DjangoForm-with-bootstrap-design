from django.contrib import admin

from myApp.models import *


admin.site.register(studentModel)
admin.site.register(teacherModel)
admin.site.register(employeeModel)
admin.site.register(NurseModel)
admin.site.register(StuffModel)