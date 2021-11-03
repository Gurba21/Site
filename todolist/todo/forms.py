from typing import Text
from django import forms
from django.forms.fields import CharField
from django.forms.widgets import Widget

class TodoForm(forms.Form):
    text = forms.CharField(max_length=255,widget=forms.TextInput(
        attrs={
        'class':'form-control',
        'planceholder':'Введите сюда свой список дел',
        'aria-label':'Todo',
        'aria-describedby':'add-btn'
    }))