from django import forms

from cart.models import (
    ProductOrder,
    Order
)


class ProductOrderForm(forms.ModelForm):
    size = forms.ChoiceField()
    color = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['size'].choices = [
            (choice, choice) for _, choice in enumerate(
                self.initial.get('size')
            )
        ]
        self.fields['color'].choices = [
            (choice, choice) for _, choice in enumerate(
                self.initial.get('color')
            )
        ]

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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['products'] = forms.CharField(
            max_length=666,
            widget=forms.widgets.HiddenInput()
        )

    class Meta:
        model = Order
        fields = (
            'products',
            'email',
            'phone',
            'adress',
            'customer_name',
        )
