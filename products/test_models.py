from django.test import TestCase
from .models import Category, Product


class TestCategoryProductModel(TestCase):
    """ Test category model """
    def test_category_model(self):
        """
        Test Category Model
        """
        category = Category.objects.create(name="test_category")
        self.assertEqual(str(category), "test_category")

    def test_product_model(self):
        """
        Test Product Model
        """
        products = Product.objects.create(
            sku='456455',
            name="test",
            description="This is a test",
            usage="test this product",
            brand="product brand",
            has_sizes=False,
            ingredients="test product quality",
            price="12.34",
            rating="5",
            )
        self.assertEqual(str(products), "test")

