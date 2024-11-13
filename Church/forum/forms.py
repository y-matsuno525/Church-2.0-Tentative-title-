from django import forms 

class DiscussionForm(forms.Form):
    text = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    