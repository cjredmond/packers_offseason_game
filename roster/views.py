from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from roster.models import Player, DraftPlayer, FreeAgent

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
