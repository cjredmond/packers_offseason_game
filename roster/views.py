from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse, reverse_lazy
from roster.models import Player, DraftPlayer, FreeAgent, Draft, CapCasualty

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        total_cap = sum([player.cap_hit for player in Player.objects.all()])
        context['qb'] = Player.objects.filter(position='QB').order_by('-cap_hit')
        context['hb'] = Player.objects.filter(position='HB').order_by('-cap_hit')
        context['wr'] = Player.objects.filter(position='WR').order_by('-cap_hit')
        context['te'] = Player.objects.filter(position='TE').order_by('-cap_hit')
        context['ol'] = Player.objects.filter(position='OL').order_by('-cap_hit')
        context['dl'] = Player.objects.filter(position='DL').order_by('-cap_hit')
        context['ed'] = Player.objects.filter(position='ED').order_by('-cap_hit')
        context['lb'] = Player.objects.filter(position='LB').order_by('-cap_hit')
        context['cb'] = Player.objects.filter(position='CB').order_by('-cap_hit')
        context['s'] = Player.objects.filter(position='S').order_by('-cap_hit')
        context['count'] = Player.objects.all().count()
        context['total_cap'] = total_cap
        context['cap_space_left'] = 171.5 - total_cap
        return context

class FreeAgentView(TemplateView):
    template_name = "free_agent.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['qb'] = FreeAgent.objects.filter(position='QB',on_team=False).order_by('-cap_hit')
        context['hb'] = FreeAgent.objects.filter(position='RB',on_team=False).order_by('-cap_hit')
        context['wr'] = FreeAgent.objects.filter(position='WR',on_team=False).order_by('-cap_hit')
        context['te'] = FreeAgent.objects.filter(position='TE',on_team=False).order_by('-cap_hit')
        context['ol'] = FreeAgent.objects.filter(position='OL',on_team=False).order_by('-cap_hit')
        context['dl'] = FreeAgent.objects.filter(position='DL',on_team=False).order_by('-cap_hit')
        context['ed'] = FreeAgent.objects.filter(position='ED',on_team=False).order_by('-cap_hit')
        context['lb'] = FreeAgent.objects.filter(position='LB',on_team=False).order_by('-cap_hit')
        context['cb'] = FreeAgent.objects.filter(position='CB',on_team=False).order_by('-cap_hit')
        context['s'] = FreeAgent.objects.filter(position='S',on_team=False).order_by('-cap_hit')
        return context

class ReSignView(TemplateView):
    template_name = "resign.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['players'] = FreeAgent.objects.filter(on_team=True)
        return context

class DraftView(DetailView):
    model = Draft
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = Draft.objects.get(id=self.kwargs['pk'])
        context['players'] = DraftPlayer.objects.filter(draft_round=subject.draft_round)
        return context

class DraftPlayerView(CreateView):
    model = Player
    fields = []
    def get_success_url(self, **kwargs):
        target = Draft.objects.first()
        if target.round == 8:
            return reverse('index_view')
        return reverse('draft_view', args=('1'))
    def form_valid(self, form):
        player_info = DraftPlayer.objects.get(id=self.kwargs['pk'])
        draft = Draft.objects.get(id=1)
        draft.draft_round += 1
        draft.save()
        instance = form.save(commit=False)
        instance.first_name = player_info.first_name
        instance.last_name = player_info.last_name
        instance.position = player_info.position
        instance.cap_hit = player_info.cap_hit
        instance.cut_savings = player_info.cap_hit / 2
        player_info.delete()
        return super().form_valid(form)

class ReSignPlayerView(CreateView):
    model = Player
    fields = []
    def get_success_url(self,**kwargs):
        return reverse('resign_view')
    def form_valid(self,form):
        player_info = FreeAgent.objects.get(id=self.kwargs['pk'])
        instance = form.save(commit=False)
        instance.first_name = player_info.first_name
        instance.last_name = player_info.last_name
        instance.position = player_info.position
        instance.cap_hit = player_info.cap_hit
        instance.cut_savings = player_info.cap_hit/2
        player_info.delete()
        return super().form_valid(form)

class FreeAgentSignView(CreateView):
    model = Player
    fields = []
    def get_success_url(self,**kwargs):
        return reverse('free_agent_view')
    def form_valid(self,form):
        player_info = FreeAgent.objects.get(id=self.kwargs['pk'])
        instance = form.save(commit=False)
        instance.first_name = player_info.first_name
        instance.last_name = player_info.last_name
        instance.position = player_info.position
        instance.cap_hit = player_info.cap_hit
        instance.cut_savings = player_info.cap_hit/2
        player_info.delete()
        return super().form_valid(form)

class CutPlayerView(DeleteView):
    model = Player
    def get_success_url(self,**kwargs):
        player_info = Player.objects.get(id=self.kwargs['pk'])
        FreeAgent.objects.create(first_name=player_info.first_name,last_name=player_info.last_name,
                                 position=player_info.position, cap_hit=player_info.cap_hit, on_team=False)
        return reverse('index_view')


import csv
def clear():
    Player.objects.all().delete()
    DraftPlayer.objects.all().delete()
    FreeAgent.objects.all().delete()

def add_team_player():
    with open('roster/packers_roster.csv') as infile:
        reader = csv.reader(infile)
        for row in reader:
            print(row[0],row[1])
            Player.objects.create(first_name=row[0],last_name=row[1],position=row[2],cap_hit=row[3],
            cut_savings=0)

def add_free_agents():
    with open('roster/free_agents.csv') as infile:
        reader = csv.reader(infile)
        for row in reader:
            print(row[0],row[1])
            FreeAgent.objects.create(first_name=row[0],last_name=row[1],position=row[2],cap_hit=row[3],on_team=row[4])

def add_draft():
    with open('roster/draft.csv') as infile:
        reader = csv.reader(infile)
        for row in reader:
            print(row[0],row[1])
            DraftPlayer.objects.create(first_name=row[0],last_name=row[1],position=row[2],cap_hit=row[3],draft_round=row[4],college=row[5])

def add_cap_casualty():
    with open('roster/cap_casualty.csv') as infile:
        reader = csv.reader(infile)
        for row in reader:
            print(row[0],row[1])
            CapCasualty.objects.create(first_name=row[0],last_name=row[1],position=row[2],cap_hit=row[3])

def draft_reset():
    draft = Draft.objects.first()
    draft.draft_round = 1
    draft.save()

def cut_players():
    x = CapCasualty.objects.all().order_by('?')
    for player in x[:20]:
        FreeAgent.objects.create(first_name=player.first_name, last_name=player.last_name,
                                 position=player.position, cap_hit=player.cap_hit, on_team=False)


def seed_db():
    clear()
    add_team_player()
    add_draft()
    add_free_agents()
    add_cap_casualty()
    cut_players()
    draft_reset()
