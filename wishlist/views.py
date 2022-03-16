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
    favourite = Wishlist.objects.get(user=request.user)

    context = {
        'favourite': favourite,
    }
    return render(request, 'wishlist/favourite.html', context)


@login_required
def add_favorites(request, product_id):
    """
    A view to allow users to add items
    to their wishlist, if it already exist 
    inform user.
    """
    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        favourite, _ = Wishlist.objects.get_or_create(user=request.user)

        if product not in favourite.products.all():
            favourite.products.add(product)
            messages.success(request,
                             (f'Successfully added {product.name} to wishlist'))
        else:
            messages.error(request,
                           (f'{product.name} already exists in wishlist'))
    return redirect('products')
