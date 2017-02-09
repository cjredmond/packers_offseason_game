from django.contrib import admin
from roster.models import Player, FreeAgent, DraftPlayer

admin.site.register([Player,FreeAgent,DraftPlayer])
