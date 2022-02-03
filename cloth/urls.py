from os import name
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('tags/', views.TagListView.as_view(), name='tags'),
    path('products/hoodie/', views.HoodieListView.as_view(), name='hoodies'),
    path('products/t-shirt/', views.TShirtListView.as_view(), name='t_shirts'),
    path('products/pant/', views.PantsListView.as_view(), name='pants'),
    path('products/shoe/', views.ShoesListView.as_view(), name='shoes'),
    path('products/<int:id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path("add-order/", views.OrderCreateView.as_view(), name="create_order"),
]
