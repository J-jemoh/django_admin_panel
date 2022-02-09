from pickle import TRUE
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Participants(models.Model):
    id=models.AutoField(primary_key=TRUE)
    participant_id = models.IntegerField()
    sex=models.CharField(max_length=50)
    age=models.IntegerField()
    enrollment_date= models.DateField()
    staff_initials = models.CharField(max_length=50)

class Viralload(models.Model):
    id=models.AutoField(primary_key=TRUE)
    participants = models.ForeignKey(Participants,on_delete=models.CASCADE)
    date_collection =models.DateField()
    vl_captured =models.IntegerField(default=1)
    vl_results=models.IntegerField()
    date_received= models.DateField()
    date_entered = models.DateField()
    staff_initials = models.CharField(max_length=50)


class Rerand(models.Model):
    id=models.AutoField(primary_key=TRUE)
    viralload =models.ForeignKey(Viralload,on_delete=models.CASCADE,default='')
    participants =models.ForeignKey(Participants, on_delete=models.CASCADE,default='')
    rerand_date=models.DateField()
    vl_results= models.CharField(max_length=50)
    rerand_arm = models.CharField(max_length=50)
    staff_initials = models. CharField(max_length=50)
class EOIC(models.Model):
    id=models.AutoField(primary_key=TRUE)
    eoic_id = models.IntegerField()
    vl_result= models.CharField(max_length=50)
    investigation_date= models.DateField()
    entry_date= models.DateField()
    staff_initials = models.CharField(max_length=50)
class VLMONTH6(models.Model):
    id=models.AutoField(primary_key=TRUE)
    rerand = models.ForeignKey(Rerand,on_delete=models.CASCADE,default='')
    participants=models.ForeignKey(Participants,models.CASCADE,default='')
    collection_date= models.DateField()
    vl_result = models.CharField(max_length=50)
    vl_suppressed = models.IntegerField()
    date_received = models.DateField()
    staff_initials = models.CharField(max_length=50)