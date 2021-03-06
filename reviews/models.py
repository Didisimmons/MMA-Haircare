from django.db import models
from profiles.models import User
from products.models import Product


class ProductReview(models.Model):
    RATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text_review = models.TextField()
    rating = models.IntegerField(choices=RATING)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Reviews'
        ordering = ['-date']

    def __str__(self):
        return self.text_review
