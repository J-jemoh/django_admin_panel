from django.db import models

# Create your models here.

class Participants(models.Model):
    participant_id = models.IntegerField()
    sex=models.CharField(max_length=50)
    age=models.IntegerField()
    enrollment_date= models.DateField()
    staff_initials = models.CharField(max_length=50)

class Viralload(models.Model):
    participants = models.ForeignKey(Participants,on_delete=models.CASCADE)
    date_collection =models.DateField()
    vl_results=models.CharField(max_length=50)
    date_received= models.DateField()
    date_entered = models.DateField()
    staff_initials = models.CharField(max_length=50)

    def __str__(self):
        return  self.participants

class Rerand(models.Model):
    rerand_id =models.IntegerField()
    rerand_date=models.DateField()
    vl_results= models.CharField(max_length=50)
    rerand_arm = models.CharField(max_length=50)
    staff_initials = models. CharField(max_length=50)
class EOIC(models.Model):
    eoic_id = models.IntegerField()
    vl_result= models.CharField(max_length=50)
    investigation_date= models.DateField()
    entry_date= models.DateField()
    staff_initials = models.CharField(max_length=50)
class VLMONTH6(models.Model):
    month6_id = models.IntegerField()
    collection_date= models.DateField()
    vl_result = models.CharField(max_length=50)
    vl_suppressed = models.CharField(max_length=50)
    date_received = models.DateField()
    staff_initials = models.CharField(max_length=50)