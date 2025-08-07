from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(label='Name', max_length=60)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    price = forms.FloatField(label='Price')

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError('Price must be greater than zero')
        return price
