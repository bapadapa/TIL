from django.contrib import admin
from django.urls import include,path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from grab import views as grab_views
from oldgrab import views as Product_View

router = DefaultRouter()
router.register('drf', grab_views.ProductViewSet)

urlpatterns = [    
    path('post/',Product_View.Product_List),
    path('post/<str:pk>',Product_View.Product_detail),
    path('admin',admin.site.urls),    
    path('',include(router.urls))
]

