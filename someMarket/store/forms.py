from django import forms

from store.models import Product


class SortProds(forms.ModelForm):
    sortby = forms.ChoiceField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sortby'].choices = (
            ('price-ascending', 'Подороже'),
            ('price-descending', 'Подешевле'),
            ('created-descending', 'Постарее'),
            ('created-ascending', 'Поновее')
        )

    class Meta:
        model = Product
        fields = (
            'sortby',
        )
