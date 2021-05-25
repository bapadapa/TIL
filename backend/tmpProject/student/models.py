from django.db import models

# Create your models here.
class Student(models.Model):
    # s_name = varchar형이고, 최대 길이는 30이다.
    s_name = models.CharField(max_length=30)
    s_major = models.CharField(max_length=30)
    s_age = models.IntegerField(default=0)
    s_grade = models.IntegerField(default=0)
    s_gender = models.CharField(max_length=30)
    
    def __str__(self):
        return self.s_name


#생성되는 테이블 이름 규칙 (소문자) 어플리케이션이름_클래스명 : students_student