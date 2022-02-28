from django import forms
from django.forms import widgets
from .models import Problem

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        #fields = '__all__'
        exclude = ['adopted', 'attempted', 'created_by','date_created']

        widgets = {
            'app': forms.Select(attrs={'class': "{%App%}"}), # or whatever class you want to apply
            # and so on
         }