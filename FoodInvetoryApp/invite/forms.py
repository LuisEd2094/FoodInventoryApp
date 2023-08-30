from django import forms

class InvitationForm(forms.Form):
    receiving_user = forms.CharField(max_length=150, label="Recipient User's Username")
    message = forms.CharField(widget=forms.Textarea, required=False)