from django.db import models

POSITION = [('QB','Quarterback'), ('HB', 'Running Back'), ('WR', 'Wide Receiver'),
            ('TE', 'Tight End'), ('OL', 'Offensive Line'), ('DL', 'Defensive Line'),
            ('ED', 'Edge'), ('LB', 'Inside Linebacker'), ('CB', 'Corner'),
            ('S', 'Safety')]

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=2, choices=POSITION)
    cap_hit = models.IntegerField()
    cut_savings = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.position + ' ' + self.first_name + " " + self.last_name)

class FreeAgent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=2, choices=POSITION)
    cap_hit = models.IntegerField()
    on_team = models.BooleanField()

    def __str__(self):
        return str(self.position + ' ' + self.first_name + " " + self.last_name)

class DraftPlayer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=2, choices=POSITION)
    cap_hit = models.IntegerField()
    draft_round = models.IntegerField()

    def __str__(self):
        return str(self.position + ' ' + self.first_name + " " + self.last_name)

class Draft(models.Model):
    draft_round = models.IntegerField(default=1)
