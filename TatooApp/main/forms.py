from django import forms
from .models import Image, Data

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']

class DataForm(forms.ModelForm):
    date_sign = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = Data
        fields = ['description', 'date_sign']



