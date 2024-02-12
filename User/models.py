from django.db import models
from Admin.models import *
# Create your models here.

class tbl_hours(models.Model):
    project = models.ForeignKey(tbl_project,on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    work_date = models.CharField(max_length=30)
    hour = models.IntegerField()
    date = models.DateField(auto_now_add=True)