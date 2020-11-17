from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        # fields = ['first_name', 'last_name', 'email', 'message'] # individual fields can be included this way
        fields = '__all__'  # includes all the fields from the model
