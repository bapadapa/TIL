from django.http import HttpResponseRedirect, response
from django.shortcuts import render
from django.urls import reverse
from student.models import Student

# Create your views here.
# 등록 하는 화면을 보여주는 함수
def regStudent(request):
    return render(request,'students/registerStudent.html')

# DB에 저장하는 함수
def regConstudent(request):
    # 브라우저 -> 서버 요청시 POST방식으로 입력을 받는다.
    # 일반적으로 POST는 Create시 사용.
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']    
    qs = Student(s_name = name, s_major = major,s_age = age, s_grade = grade, s_gender =gender)
    #.save를 이용하여 sql문을 생성 및 업데이트해줌.
    qs.save()   
    #Redirect를 사용하여 중복선언을 방지함
    #DB에 저장하는 로직 실행시 꼭 넣을것! 안 넣으면 새로고침시 지속적으로 DB에 재등록함!
    return HttpResponseRedirect(reverse('student:stuAll'))

# read DB읽어오는 함수 
# select * from Student
def readStudentAll(request):    
    qs = Student.objects.all()
    context = {'student_list':qs}
    return render(request, 'students/readStudents.html',context)

#학생 상세 정보 
#select * from Student where s_name = name
def detailStudent(request, name):
    qs = Student.objects.get(s_name = name)
    context = {'student_info': qs}
    return render(request, 'students/detailStudent.html', context)   
   
def readStudent(request, name):
    qs = Student.objects.get(s_name = name)
    context = {'student_info': qs}
    return render(request, 'students/modifyStudent.html', context)
   
def modConStudent(request):
    # 아래 변수명을 models.Student에 선언한것과 잘 비교하자!
    s_qs = Student.objects.get(s_name = request.POST['name'])    
    s_qs.s_major = request.POST['major']
    s_qs.s_age = request.POST['age']
    s_qs.s_grade = request.POST['grade']
    s_qs.s_gender = request.POST['gender']       
    s_qs.save()
    
    return HttpResponseRedirect(reverse('student:stuAll'))    
    
def delConStudent(request, name):
    qs = Student.objects.get(s_name = name)
    qs.delete()
    return HttpResponseRedirect(reverse('student:stuAll'))