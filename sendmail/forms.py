from django import forms
from .models import send_mail



class send_mail_from(forms.ModelForm):

    mail_list = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label="Select E-Mail Addresses: ")

    class Meta:
        model = send_mail
        fields=[
            'subject',
            'mail_list',
            'message',
        ]