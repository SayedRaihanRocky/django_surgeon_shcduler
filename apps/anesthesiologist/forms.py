from django import forms
from apps.anesthesiologist.models import anesthesiologist


class AnesthesiologistForm(forms.ModelForm):
    class Meta:
        model = anesthesiologist
        fields = "__all__"