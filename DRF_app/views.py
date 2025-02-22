from django.shortcuts import render
from .ser import BookSerializer
from django.http import JsonResponse
from .models import Book

def book_api(request):
     if request.method == 'GET':
        data = Book.objects.all() 
        ser  = BookSerializer( data, many=True )
        return JsonResponse( ser.data, safe=False )
