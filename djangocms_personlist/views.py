from django.shortcuts import render
from django.views.generic import ListView, DetailView
from djangocms_personlist.filters import TeamMemberFilter
from .models import Team, Person


class TeamListView(ListView):
    """
    A complete list of the personlist items
    """
    model = Person
    template_name = 'djangocms_personlist/team_index.html'
    filter_class = TeamMemberFilter

    def get_queryset(self):
        q = super(TeamListView, self).get_queryset()
        return self.filter_class(self.request.GET, q)

    def get_context_data(self, **kwargs):
        context = super(TeamListView, self).get_context_data(**kwargs)
        context['teams'] = Team.objects.all()
        if self.request.GET.get('team'):
            filter_teams = self.request.GET.get('team')
            filter_teams = filter_teams.split(',')
            context['filter_teams'] = filter_teams
        else:
            context['show_all'] = True
        return context


class PersonDetailView(DetailView):
    """
    Detail view of a personlist item
    """
    model = Person
    template_name = 'djangocms_personlist/person_detail.html'


