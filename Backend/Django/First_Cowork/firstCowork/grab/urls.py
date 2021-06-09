from firstCowork import oldgrab
from django.urls import include,path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from . import views as grab_views

router = DefaultRouter()
router.register('drf', grab_views.ProductViewSet)

urlpatterns = [

]

