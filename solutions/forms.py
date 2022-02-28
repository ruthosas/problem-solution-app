from django import forms
from .models import Solution

class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        #fields = '__all__'
        exclude = ['created_by','date_created']