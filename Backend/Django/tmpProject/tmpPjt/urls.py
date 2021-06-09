"""tmpPjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include('student.urls') ),

    # 아래 path들을 지역변수로 만들어버림
    # student로 옮김

    # path('jobs/', hr_views.list_jobs),
    # path('reg/',s_views.regStudent, name = 'reg'),
    # path('regCon/',s_views.regConstudent, name ='regCon'),
    # path('all/',s_views.readStudentAll, name= 'stuAll'),
    # path('det/',s_views.detailStudent, name =''),
    

]
