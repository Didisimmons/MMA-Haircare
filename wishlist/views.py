from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib.auth.decorators import login_required
from products.models import Product

from django.contrib import messages

from .models import Wishlist


@login_required
def favorites(request):
    """ A view to return users wishlist """
    favourite = Wishlist.objects.filter(user=request.user)

    context = {
        'favourite': favourite,
    }
    return render(request, 'wishlist/favourite.html', context)


@login_required
def add_favorites(request, product_id):
    """
    A view to allow users to add items
    to their wishlist.
    """
    product = get_object_or_404(Product, pk=product_id)
    favourite = Wishlist.objects.filter(user=request.user)
    
    if request.user.is_authenticated:
        favourite, _ = Wishlist.objects.get_or_create(user=request.user)
        favourite.products.add(product)
    messages.info(request, 'Successfully Added to your wishlist')
    return redirect(reverse('favorites'))
