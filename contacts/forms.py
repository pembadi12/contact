
from django import forms

from contacts.models import Contact


class contactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['name','email']