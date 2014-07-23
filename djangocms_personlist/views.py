from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Team, Person


class TeamListView(ListView):
    """
    A complete list of the personlist items
    """
    model = Team
    template_name = 'djangocms_personlist/team_list.html'


class TeamDetailView(DetailView):
    """
    Detail view of a personlist item
    """
    model = Team
    template_name = 'djangocms_personlist/team_detail.html'


class PersonListView(ListView):
    """
    A complete list of the personlist items
    """
    model = Person
    template_name = 'djangocms_personlist/person_list.html'


class PersonDetailView(DetailView):
    """
    Detail view of a personlist item
    """
    model = Person
    template_name = 'djangocms_personlist/person_detail.html'


