from django.db import models
from apps.pateint.models import patient
from apps.sergeon.models import Surgeon
from apps.anesthesiologist.models import anesthesiologist



class pateingsurgeryscheduler(models.Model):

    schedule_code = models.CharField(max_length=20)
    schedule_name = models.CharField(max_length=100)
    pateint_id = models.ForeignKey(patient, blank=True, null=True, on_delete=models.SET_NULL)
    surgeon_id = models.ForeignKey(Surgeon, blank=True, null=True, on_delete=models.SET_NULL)
    anesthesiologist_id = models.ForeignKey(anesthesiologist, blank=True, null=True, on_delete=models.SET_NULL)
    schedule_date = models.DateTimeField()
    schedule_status = models.BooleanField()

    class Meta:
        db_table = "pateintsurgeryschedule"

