from django.urls import path
from .views import book_api, book_api2
urlpatterns = [
    path('', book_api, name='book_api'),
    path('book_api2', book_api2, name="book_api2")
]
