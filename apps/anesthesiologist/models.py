from django.db import models

# Create your models here.

from django.db import models


class anesthesiologist(models.Model):

    a_code = models.CharField(max_length=20)
    a_name = models.CharField(max_length=100)
    a_email = models.EmailField()
    a_contact = models.CharField(max_length=15)
    a_address = models.CharField(max_length=250)
    a_highest_degree = models.CharField(max_length=150)
    rate_per_day = models.FloatField()
    rate_per_surgery = models.FloatField()
    sg_status = models.BooleanField()

    class Meta:
        db_table = "infoanesthesiologist"

    def __str__(self):
        return "%s" % (self.a_name)

