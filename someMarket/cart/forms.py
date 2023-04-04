from django import forms

from cart.models import (
    ProductOrder,
    Order
)


class ProductOrderForm(forms.ModelForm):
    """Форма, построенная на модели ProductOrder, используется для
    оформления продуктов заказа из корзины сессии юзера.
    """

    size = forms.ChoiceField(label='Размер')
    color = forms.ChoiceField(label='Цвет')

    def __init__(self, *args, **kwargs):
        """Здесь, из стандартных CharField'ов полей 'size' и
        'color' делаем ChoiceField.
        """

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
        self.fields['count'].label = 'Количество'

    class Meta:
        model = ProductOrder
        fields = (
            'product_id',
            'size',
            'color',
            'count'
        )
        widgets = {
            'product_id': forms.HiddenInput()
        }


class OrderForm(forms.ModelForm):
    """Форма, для оформления заказов, кастомизируем поля
    'phone' и 'customer_name' .
    """

    email = forms.EmailField(required=False, label='Почта')
    phone = forms.RegexField(
        r'^\+?1?\d{11}$',
        label='Телефон'
    )
    customer_name = forms.RegexField(
        r'^[А-ЯЁ][а-яё]*([-][А-ЯЁ][а-яё]*)?\s[А-ЯЁ][а-яё]*\s[А-ЯЁ][а-яё]*$',
        label='Фамилия Имя Отчество'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['adress'].label = 'Адрес'

    class Meta:
        model = Order
        fields = (
            'phone',
            'adress',
            'customer_name',
        )
