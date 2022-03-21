from django.urls import path
from . import views

urlpatterns = [
    path("add/<product_id>", views.add_reviews, name="add_reviews"),
    path('delete/<int:review_id>/', views.delete_reviews,
         name='delete_reviews'),
    path('edit/<int:review_id>/', views.edit_reviews,
         name='edit_reviews'),
]
