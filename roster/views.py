from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from roster.models import Player

class IndexView(TemplateView):
    template_name = "index.html"
