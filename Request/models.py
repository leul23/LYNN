from django.db import models

# Create your models here.

class requests(models.Model):

   username = models.CharField(max_length = 50)
   request = models.CharField(max_length = 50)
   location = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()

   class Meta:
      db_table = "Requests"