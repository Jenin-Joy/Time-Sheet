from django.db import models

# Create your models here.

class tbl_admin(models.Model):
    admin_name = models.CharField(max_length=30)
    admin_contact = models.CharField(max_length=30)
    admin_email = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=30)

class tbl_type(models.Model):
    type_name = models.CharField(max_length=30)

class tbl_project(models.Model):
    project_name = models.CharField(max_length=30)
    project_description = models.CharField(max_length=30)
    project_status = models.IntegerField()
    type_id = models.ForeignKey(tbl_type,on_delete=models.CASCADE)

class tbl_user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    role = models.CharField(max_length=30)