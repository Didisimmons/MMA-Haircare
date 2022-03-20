from django.urls import path
from . import views

urlpatterns = [
    path("reviews", views.reviews, name="reviews"),
    path("reviews/<product_id>", views.add_reviews, name="add_reviews"),
]
