from django import forms

from apps.sergeon.models import Surgeon


class SurgeonForm(forms.ModelForm):
    class Meta:
        model = Surgeon
        fields = "__all__"
