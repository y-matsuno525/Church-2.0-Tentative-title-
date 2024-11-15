from django import forms 

class DiscussionForm(forms.Form):
    text = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

class PageForm(forms.Form):
    page_number = forms.IntegerField(label="Enter Chapter Number",required=True)