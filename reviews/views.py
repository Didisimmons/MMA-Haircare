from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from django.contrib import messages

from .models import ProductReview
from .models import Product
from .forms import ProductReviewForm


@login_required
def reviews(request):
    """ A view to display users review  """
    review = ProductReview.objects.filter(user=request.user).order_by('-id')

    context = {
        'review': review,
    }
    return render(request, 'reviews/reviews.html', context)


def add_reviews(request, product_id):
    """
    Allow user to add review to product
    """
    user = get_object_or_404(UserProfile, user=request.user)
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.product = product
            review.save()
            messages.success(request, 'Successfully added Product review')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Sorry we cannot add Product review. \
                                     Please ensure all fields are completed.')

    context = {
        'form': form,
    }

    return render(request, context)
