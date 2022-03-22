from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from django.contrib import messages

from .models import ProductReview
from .models import Product
from .forms import ProductReviewForm


@login_required
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


@login_required
def delete_reviews(request, review_id):
    """ Delete review from the store"""

    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product

    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def edit_reviews(request, review_id):
    """
    Allow user to edit their reviews
    """
    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product
    if request.method == 'POST':
        form = ProductReviewForm(request.POST, instance=review)
        if form.is_valid():
            review.save()
            messages.success(request, 'Successfully updated Product review')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Sorry we cannot update Product review. \
                                     Please ensure all fields are completed.')
    else:
        form = ProductReviewForm(instance=review)

    template = 'products/product_detail.html'

    context = {
        'form': form,
        'review': review,
        'product': product,
    }

    return render(request, template, context)


@login_required
def dit_reviews(request, review_id):

    review = ProductReview.objects.get(user=request.user)
    review_form = ProductReviewForm(initial={
        'text_review': review.text_review,
        'rating': review.rating,
    })

    if request.method == 'POST':
        form = ProductReviewForm(review_form, instance=review)
        if form.is_valid():
            review.save()
            messages.success(request, 'Successfully updated Product review')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Sorry we cannot update Product review. \
                                    Please ensure all fields are completed.')
    else:
        form = ProductReviewForm(instance=review)

    template = 'products/product_detail.html'

    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)
