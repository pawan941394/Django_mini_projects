from django import forms
from .models import create
from ckeditor.widgets import CKEditorWidget

class createform(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(),label="Text Editor")
    class Meta:
        model = create
        fields = {'body'}
