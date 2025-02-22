from django.shortcuts import render
from .ser import BookSerializer, UserSerializer
from django.http import JsonResponse
from .models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
@api_view( [ 'GET', 'POST'] )

def book_api(request):
     if request.method == 'GET':
        data = Book.objects.all() 
        ser  = BookSerializer( data, many=True )
        return JsonResponse( ser.data, safe=False )

@api_view(['GET', 'POST'])
def book_api2(request):
    match request.method:
        case 'GET':
            data = Book.objects.all()
            ser = BookSerializer(data, many=True)
            return Response(ser.data)
        case 'POST':
            ser = BookSerializer(data=request.data)
            if ser.is_valid():
               ser.save()
            data = Book.objects.all()  
            ser = BookSerializer(data, many=True)
            return Response(ser.data)
         



@api_view(['GET', 'POST'])
def create_user(request):
    match request.method:
        case 'GET':
            data = User.objects.all()
            ser = UserSerializer(data, many=True)
            return Response(ser.data)
        case 'POST':
            ser = UserSerializer(data=request.data)
            if ser.is_valid():
               ser.save()
            data = User.objects.all()  
            ser = UserSerializer(data, many=True)
            return Response(ser.data)
            
  
