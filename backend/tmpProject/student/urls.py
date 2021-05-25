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

from django.urls import path
import student.views as s_views

app_name = 'student'
urlpatterns = [
    path('reg/',s_views.regStudent, name = 'reg'),
    path('regCon/',s_views.regConstudent, name ='regCon'),
    path('all/',s_views.readStudentAll, name= 'stuAll'),
    path('<str:name>/det/',s_views.detailStudent, name ='stuDet'),
    path('<str:name>/mod/',s_views.readStudent,name = 'stuMod'),
    path('modCon/',s_views.modConStudent,name = 'modCon'),
    path('<str:name>/del/',s_views.delConStudent,name = 'stuDel'),
    

]
