from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from roster.models import Player, DraftPlayer, FreeAgent

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        total_cap = sum([player.cap_hit for player in Player.objects.all()])
        context['qb'] = Player.objects.filter(position='QB')
        context['hb'] = Player.objects.filter(position='RB')
        context['wr'] = Player.objects.filter(position='WR')
        context['te'] = Player.objects.filter(position='TE')
        context['ol'] = Player.objects.filter(position='OL')
        context['dl'] = Player.objects.filter(position='DL')
        context['ed'] = Player.objects.filter(position='ED')
        context['lb'] = Player.objects.filter(position='LB')
        context['cb'] = Player.objects.filter(position='CB')
        context['s'] = Player.objects.filter(position='S')
        context['count'] = Player.objects.all().count()
        context['total_cap'] = total_cap
        context['cap_space_left'] = 176 - total_cap
        return context

class FreeAgentView(TemplateView):
    template_name = "free_agent.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['qb'] = FreeAgent.objects.filter(position='QB',on_team=False)
        context['hb'] = FreeAgent.objects.filter(position='RB',on_team=False)
        context['wr'] = FreeAgent.objects.filter(position='WR',on_team=False)
        context['te'] = FreeAgent.objects.filter(position='TE',on_team=False)
        context['ol'] = FreeAgent.objects.filter(position='OL',on_team=False)
        context['dl'] = FreeAgent.objects.filter(position='DL',on_team=False)
        context['ed'] = FreeAgent.objects.filter(position='ED',on_team=False)
        context['lb'] = FreeAgent.objects.filter(position='LB',on_team=False)
        context['cb'] = FreeAgent.objects.filter(position='CB',on_team=False)
        context['s'] = FreeAgent.objects.filter(position='S',on_team=False)
        return context

class ReSignView(TemplateView):
    template_name = "resign.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['players'] = FreeAgent.objects.filter(on_team=True)
        return context
