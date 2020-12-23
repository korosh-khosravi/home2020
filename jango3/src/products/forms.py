from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'placeholder': 'my title'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'placeholder' : 'my description',
                                          'class' : 'new-class-name two',
                                          'id' : 'my-id-for-text-area',
                                          'rows' : 12,
                                          'cols' : 45
                                      }))
    email = forms.EmailField()
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if 'CFE' in title:
            return title
        else:
            raise forms.ValidationError('this is not valid')

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith("edu"):
            raise forms.ValidationError('this is not valid email')
        return email


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'my title'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          'placeholder': 'my description',
                                          'class': 'new-class-name two',
                                          'id': 'my-id-for-text-area',
                                          'rows': 12,
                                          'cols': 45
                                      }))
    price = forms.DecimalField()
