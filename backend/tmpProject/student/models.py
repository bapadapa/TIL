from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=30)
    s_major = models.CharField(max_length=30)

#생성되는 테이블 이름 규칙 (소문자) 어플리케이션이름_클래스명 : students_student