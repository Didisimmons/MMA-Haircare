from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Wishlist(models.Model):
    """
    displays product items in users wishlist
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,
                                      through="WishlistItem",
                                      related_name='liked_items')

    def __str__(self):
        return self.user.username


class WishlistItem(models.Model):
    """
    allows users to add product items to
    favourites.
    """
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    favourites = models.ForeignKey(Wishlist, null=False,
                                   blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
