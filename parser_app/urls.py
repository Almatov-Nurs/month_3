from os import name
from django.urls import path
from . import views

app_name = 'parse'

urlpatterns = [
    path('parser/', views.ParserFormView.as_view(), name='parser_form'),
    path('parser/list/', views.ParseListView.as_view(), name='parse_list'),
    path('parser/list/<int:id>/', views.ParseDetailView.as_view(), name='parse_detail'),
]