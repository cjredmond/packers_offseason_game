from django.contrib import admin
from roster.models import Player, FreeAgent, DraftPlayer, Draft

admin.site.register([Player,FreeAgent,DraftPlayer,Draft])
