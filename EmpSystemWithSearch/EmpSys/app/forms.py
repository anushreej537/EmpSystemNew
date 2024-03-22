from django import forms
from .models import *

class EmpForm(forms.ModelForm):
    class Meta:
        model = EmpDetail
        fields = '__all__'