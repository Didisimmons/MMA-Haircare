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
        Test Category Model
        """
        category = Category.objects.create(name="test_category")
        self.assertEqual(str(category), "test_category")

