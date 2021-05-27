from django.http.response import ResponseHeaders
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,generics
from .models import  Message
from .serializers import MessageSerializer

# Create your views here.
class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all(many =True)
    serializer_class =MessageSerializer

@APIView(['GET'])
def get_list_Message(request):
    Serializer = MessageSerializer(Message.objects.all(),many=True)
    return ResponseHeaders(Serializer.data)