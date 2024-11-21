from mdeditor.fields import MDTextFormField
from django import forms 

class PreprintForm(forms.Form):
    title = forms.CharField()
    abstract = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    content = MDTextFormField()

