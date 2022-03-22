from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):
    """ Test product form  """
    def test_sku_field_is_not_required(self):
        form = ProductForm({'sku': ''})
        self.assertFalse(form.is_valid())
