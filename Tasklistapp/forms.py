from django import forms
from .models import Alltask

class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Alltask
        fields = ['task','done']