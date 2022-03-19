from django.urls import path
from . import views

urlpatterns = [
    path("reviews/<product_id>", views.reviews, name="reviews"),
]
