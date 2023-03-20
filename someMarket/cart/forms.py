from django import forms

from store.models import (
    Color,
    Size,
    Count,
    Product
)
from cart.models import (
    ProductOrder,
    Order
)


class ProductOrderForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    # sizes1 = forms.ModelChoiceField(queryset=Size.objects.all())
    size = forms.ChoiceField()
    color = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['size'].choices = [(i, choice) for i, choice in enumerate(self.initial.get('size'))]
        self.fields['color'].choices = [(i, choice) for i, choice in enumerate(self.initial.get('color'))]

    class Meta:
        model = ProductOrder
        fields = (
            'product',
            'size',
            'color',
            'count'
        )
        widgets = {
            'product': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

