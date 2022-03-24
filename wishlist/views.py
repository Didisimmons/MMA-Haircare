from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.contrib.auth.models import User

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
        favourite, created = Wishlist.objects.get_or_create(user=request.user)

        if product not in favourite.products.all():
            favourite.products.add(product)
            messages.info(request,
                          (f'Successfully added {product.name} to wishlist'))
        else:
            messages.error(request,
                           (f'{product.name} already exists in wishlist'))
    return redirect(reverse('products'))


@login_required
def remove_favorites(request, product_id):
    """
    A view to allow users to remove items
    from their wishlist.
    """
    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        favourite = Wishlist.objects.get(user=request.user)

        if product in favourite.products.all():
            favourite.products.remove(product)
            messages.info(request,
                          (f'Successfully removed {product.name} '
                           f'from wishlist'))
        else:
            messages.error(request,
                           (f'{product.name} already removed'))
    return redirect(reverse('favorites'))




def avorites(request):
    """ A view to return users wishlist """
    favourite = Wishlist.objects.filter(user=user)
    profile = None

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)

    print(favourite)
    context = {
        'favourite': favourite,
        'profile': profile
    }
    return render(request, 'wishlist/favourite.html', context)