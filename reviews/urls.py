from django.urls import path
from . import views

urlpatterns = [
    path("add/<product_id>", views.add_reviews, name="add_reviews"),
    path('delete/<int:product_id>/', views.delete_reviews,
         name='delete_reviews'),
]
