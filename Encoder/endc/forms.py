from django import forms
class encorder(forms.Form):
    text = forms.CharField(label='',widget=forms.TextInput(attrs={'id':'text','class':'form-control' }))

