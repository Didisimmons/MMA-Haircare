from django import forms
from .models import ProductReview


class ProductReviewForm(forms.ModelForm):
    """ Form to allow users to add reviews to each product """
    class Meta:
        model = ProductReview
        fields = ('text_review', 'rating')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text_review'].label = "Review"
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-grey rounded-0'
