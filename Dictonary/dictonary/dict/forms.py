from django import forms

class searchForm(forms.Form):
    search = forms.CharField(label='Your name', max_length=100)