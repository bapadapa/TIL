from django.db import models

# Create your models here.
# select job_id, job_title,min_salary,max_salary from jobs;
class Job(models.Model):
    job_id = models.CharField(max_length=10,primary_key=True)
    job_title = models.CharField(max_length=50, null = True)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    class Meta:
         db_table = "jobs"


class Employees(models.Model):
    pass