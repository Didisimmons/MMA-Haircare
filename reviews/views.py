from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import ProductReview


@login_required
def reviews(request):
    """ A view to return users wishlist """
    reviews = ProductReview.objects.filter(user=request.user)

    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/freviews.html', context)
