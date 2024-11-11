from django import forms 

class DiscussionForm(forms.Form):
    text = forms.CharField(label="text")
    