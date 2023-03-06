from django import forms
from application.models import AppModel


class AppModelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'style': 'background: red;'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'style': 'background: red;'}))
    class Meta:
        model = AppModel
        fields = ['name', 'image']
        