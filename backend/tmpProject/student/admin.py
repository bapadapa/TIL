from django.contrib import admin
from student.models import Student
# Register your models here.
# Django의 admin을 이용하여 DB를 관리하려면 아래와 같이 Model을 인식시켜줘야한다.
admin.site.register(Student)
