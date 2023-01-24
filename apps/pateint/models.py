from django.db import models

# Create your models here.

from django.db import models


class patient(models.Model):

    p_code = models.CharField(max_length=20)
    p_fname = models.CharField(max_length=100)
    p_lname = models.CharField(max_length=100)
    p_contact = models.CharField(max_length=200)
    p_email = models.EmailField()
    p_dob = models.DateField()
    p_address = models.CharField(max_length=250)
    p_insuarance_id = models.CharField(max_length=150)
    p_insuarance_name = models.CharField(max_length=150)
    p_status = models.BooleanField()

    class Meta:
        db_table = "infopateint"

    def __str__(self):
        return "%s %s" % (self.p_fname, self.p_lname)

