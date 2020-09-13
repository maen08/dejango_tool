from django import forms
from .models import Fullname


class FullnameForm(forms.ModelForm):
    class Meta:
        model = Fullname
        fields = ('name',)
