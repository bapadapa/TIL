from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product
from . import views as grab_view
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class =ProductSerializer

@api_view(['POST'])
def upload_image(request):
    if 'image' in request.FILES:
        file =request.FILES['image']
        filename = file._name
        file_url = '%s%s' %('static/images/',filename)
        fp =open('%s%s' %('./static/images/',filename),'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
        imageUrl = {'ImageUrl' : file_url}
        return Response(imageUrl,status = status.HTTP_201_CREATED)
    else:
        return Response({'message':'Failed to Upload File'})
