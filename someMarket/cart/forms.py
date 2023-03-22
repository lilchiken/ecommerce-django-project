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
    size = forms.ChoiceField()
    color = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['size'].choices = [(choice, choice) for i, choice in enumerate(self.initial.get('size'))]
        self.fields['color'].choices = [(choice, choice) for i, choice in enumerate(self.initial.get('color'))]

    class Meta:
        model = ProductOrder
        fields = (
            'product_id',
            'product',
            'size',
            'color',
            'count'
        )
        widgets = {
            'product': forms.TextInput(attrs={'readonly': 'readonly'}),
            'product_id': forms.HiddenInput()
        }


class OrderForm(forms.ModelForm):
    # products = forms.Field()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['products'].initial = self.data['products']
        # print(self.data['products'])
        self.

        
    class Meta:
        model = Order
        fields = (
            # 'products',
            'email',
            'phone',
            'adress',
            'customer_name',
        )
        widgets = {
            # 'products': forms.TextInput(attrs={'readonly': 'readonly'})
        }
