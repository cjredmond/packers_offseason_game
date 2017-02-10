from roster.models import Draft, Player, DraftPlayer, FreeAgent
import csv

def clear():
    Player.objects.all().delete()
    DraftPlayer.objects.all().delete()
    FreeAgent.objects.all().delete()

def add_team_player():
    with open('roster/packers_roster.csv') as infile:
        reader = csv.reader(infile)
        for row in reader:
            Player.objects.create(first_name=row[0],last_name=row[1],position=row[2],cap_hit=row[3],
            cut_savings=0)

def add_free_agents():
    with open('roster/free_agents.csv') as infile:
        reader = csv.reader(infile)
        for row in reader:
            FreeAgent.objects.create(first_name=row[0],last_name=row[1],position=row[2],cap_hit=row[3],on_team=row[4])

def add_draft():
    with open('roster/draft.csv') as infile:
        reader = csv.reader(infile)
        for row in reader:
            DraftPlayer.objects.create(first_name=row[0],last_name=row[1],position=row[2],cap_hit=row[3],draft_round=row[4],college=row[5])

def draft_reset():
    draft = Draft.objects.first()
    draft.round = 1
    draft.save()
