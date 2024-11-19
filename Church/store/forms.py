from django import forms 

class DiscussionForm(forms.Form):
    
    quantity = forms.IntegerField(required=True, min_value=1)
    