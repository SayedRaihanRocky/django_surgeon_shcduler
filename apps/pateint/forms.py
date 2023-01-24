from django import forms

from apps.pateint.models import patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = "__all__"