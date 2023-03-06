from django import forms
from application.models import AppModel


class AppModelForm(forms.ModelForm):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'style': 'background:red;'}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'style': 'background:blue'}))
    class Meta:
        model = AppModel
        fields = ['name', 'image']
        