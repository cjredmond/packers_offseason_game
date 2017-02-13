from django.contrib import admin
from roster.models import Player, FreeAgent, DraftPlayer, Draft, CapCasualty, Account

admin.site.register([Player,FreeAgent,DraftPlayer,Draft,CapCasualty, Account])
