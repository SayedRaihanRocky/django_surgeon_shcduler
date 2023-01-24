from django import forms

from apps.pateintsurgeryschedule.models import pateingsurgeryscheduler


class PateintSurgeryScheduleForm(forms.ModelForm):
    class Meta:
        model = pateingsurgeryscheduler
        fields = "__all__"
