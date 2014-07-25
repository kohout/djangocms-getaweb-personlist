from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Team, Person, PersonImage


class TeamIndexView(ListView):
    """
    A complete list of the personlist items
    """
    model = Person
    template_name = 'djangocms_personlist/team_index.html'

    def get_context_data(self, **kwargs):
        context = super(TeamIndexView, self).get_context_data(**kwargs)
        context['filter_list'] = Team.objects.all()
        return context


class TeamListView(ListView):
    """
    A filtered list of the personlist items
    """
    model = Team
    template_name = 'djangocms_personlist/team_list.html'


class PersonDetailView(DetailView):
    """
    Detail view of a personlist item
    """
    model = Person
    template_name = 'djangocms_personlist/person_detail.html'


