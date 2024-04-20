from django import forms


services = [('event_management', 'Event Management'),
            ('event_entertainment', 'Event Entertainment'),
            ('event_production', 'Event Production')
]
class ContactForm(forms.Form):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    subject = forms.ChoiceField(required=True, choices=services)
    message = forms.CharField(widget=forms.Textarea, required=True)