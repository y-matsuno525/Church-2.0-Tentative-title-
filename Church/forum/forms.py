from django import forms 

class DiscussionForm(forms.Form):
    name = forms.CharField(label="name")
    text = forms.CharField(label="text")
    