from django import forms
from .models import Frase

class FraseForm(forms.ModelForm):
    class Meta:
        model=Frase
        fields = '__all__'