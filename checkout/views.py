from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Shopping Bag is currently empty")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_k00xao0P5r64RAYcBGuR9enF002XDNTq52',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
