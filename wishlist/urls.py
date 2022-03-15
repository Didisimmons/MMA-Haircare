from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorites, name='favorites'),
    path('add/<int:product_id>/', views.add_favorites, name='add_favorites'),
]
