from django import forms 

class DiscussionForm(forms.Form):
    
    text = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

class DiscussionForm_guest(forms.Form):
    guest_name = forms.ChoiceField(label="Guest name",widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px;'}))
    text = forms.CharField(label="Content", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))


class PageForm(forms.Form):
    page_number = forms.IntegerField(label="Enter Chapter Number",required=True)


