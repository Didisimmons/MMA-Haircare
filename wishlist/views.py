from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from products.models import Product
from .models import Wishlist


def favourites(request):
    """ A view to return users wishlist """
    return render(request, 'wishlist/favourite.html')
