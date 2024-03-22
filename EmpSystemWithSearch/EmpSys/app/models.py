from django.db import models

class EmpDetail(models.Model):
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    dept = models.CharField(max_length=250)
    esal = models.IntegerField(default=0)
    bonus = models.IntegerField()
    mobile = models.IntegerField(default=0)
    role = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
