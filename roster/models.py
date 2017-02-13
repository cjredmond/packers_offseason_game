from django.db import models

POSITION = [('QB','Quarterback'), ('HB', 'Running Back'), ('WR', 'Wide Receiver'),
            ('TE', 'Tight End'), ('OL', 'Offensive Line'), ('DL', 'Defensive Line'),
            ('ED', 'Edge'), ('LB', 'Inside Linebacker'), ('CB', 'Corner'),
            ('S', 'Safety')]

class Account(models.Model):
    user = models.OneToOneField('auth.User')
    cap_max = models.FloatField(default=171.5)
    resign = models.BooleanField(default=False)
    free_agent = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    final_cuts = models.BooleanField(default=False)
    

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=2, choices=POSITION)
    cap_hit = models.FloatField()
    dead_money = models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.position + ' ' + self.first_name + " " + self.last_name)

class FreeAgent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=2, choices=POSITION)
    cap_hit = models.FloatField()
    on_team = models.BooleanField()

    def __str__(self):
        return str(self.position + ' ' + self.first_name + " " + self.last_name)

class DraftPlayer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=2, choices=POSITION)
    cap_hit = models.FloatField()
    draft_round = models.IntegerField()
    college = models.CharField(max_length=100)

    def __str__(self):
        return str(self.position + ' ' + self.first_name + " " + self.last_name)

class CapCasualty(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=2, choices=POSITION)
    cap_hit = models.FloatField()

    def __str__(self):
        return str(self.position + ' ' + self.first_name + " " + self.last_name)

class Draft(models.Model):
    draft_round = models.IntegerField(default=1)
