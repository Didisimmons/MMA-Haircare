from django.contrib import admin
from .models import ProductReview


class ProductReviewAdmin(admin.ModelAdmin):
    """ Display reviews by user """
    list_display = (
        'user',
        'product',
        'rating',
        'date',
    )

    ordering = ('-date', 'product',)


admin.site.register(ProductReview, ProductReviewAdmin)
