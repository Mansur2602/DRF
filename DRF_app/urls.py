from django.urls import path
from .views import book_api, book_api2, create_user
urlpatterns = [
    path('', book_api, name='book_api'),
    path('book_api2', book_api2, name="book_api2"),
    path("create_user", create_user, name='create_user')
]
