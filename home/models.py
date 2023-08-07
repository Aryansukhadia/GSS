

from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    subject = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateField()
    
    

class Login(models.Model):
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    date = models.DateField()
    
class Signup(models.Model):
    username = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    password = models.CharField(max_length=20)
    confirmpassword = models.CharField(max_length=20)
    date = models.DateField()
    

class Upcomingmatch(models.Model):
    team1=models.CharField(max_length=40)
    team2=models.CharField(max_length=40)
    ma_venue=models.CharField( max_length=40,default="")
    ma_date=models.DateField()
    ma_time=models.TimeField()
    ma_desc=models.TextField()
    def _str_(self):
        return self.team1
    
class Teams(models.Model):
    te_name=models.CharField(max_length=40)
    te_trophies=models.IntegerField()
    team_home=models.CharField(max_length=30,default="")
    def _str_(self):
        return self.te_name
players_types=(
    ('one','chaser'),
    ('two','keeper'),
    ('three','beaters'),
    ('four','seeker'))


class Ticket(models.Model):
    username = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    match = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField()
    address = models.TextField()
    date = models.DateField()

class Merchandise(models.Model):
    username = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    match = models.IntegerField()
    quantity = models.IntegerField()
    address = models.TextField()
    date = models.DateField()
