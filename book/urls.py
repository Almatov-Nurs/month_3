from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('book/',views.book_all, name='book_all'),
    path('book/<int:id>/',views.book_detail, name='book_detail'),
    path('add-book/',views.add_book, name='add-book')
]
