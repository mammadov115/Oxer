from .models import Message
from django import forms

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "number": forms.TextInput(attrs={"placeholder": "Phone Number"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "message": forms.TextInput(attrs={"class": "message-box", "placeholder": "Message"})
        }