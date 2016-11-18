from django.db import models
import pymysql
pymysql.install_as_MySQLdb()

class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    stake = models.FloatField()
    contacts = models.CharField(max_length=50)
    bank_account = models.CharField(max_length=50)
    
class Horse(models.Model):
    horse_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    ratio = models.FloatField()