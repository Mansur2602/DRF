from django.shortcuts import render
from .ser import BookSerializer
from django.http import JsonResponse
from .models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
         


