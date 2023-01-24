from django.db import models


class Surgeon(models.Model):
    sg_id = models.CharField(max_length=20)
    sg_code = models.CharField(max_length=20)
    sg_name = models.CharField(max_length=100)
    sg_email = models.EmailField()
    sg_contact = models.CharField(max_length=15)
    sg_address = models.CharField(max_length=250)
    sg_highest_degree = models.CharField(max_length=150)
    sg_office_name = models.CharField(max_length=150)
    sg_status = models.BooleanField()

    class Meta:
        db_table = "infosurgeon"

    def __str__(self):
        return "%s" % (self.sg_name)
