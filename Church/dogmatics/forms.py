from mdeditor.fields import MDTextFormField
from django import forms 

class PreprintForm(forms.Form):
    title = forms.CharField()
    content = MDTextFormField()

