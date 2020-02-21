from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)