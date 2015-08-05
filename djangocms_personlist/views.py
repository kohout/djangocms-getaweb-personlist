from django.db.models.query_utils import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from djangocms_personlist.filters import TeamMemberFilter
from .models import Team, Person

try:
    # >= Django 1.7
    from django.contrib.sites.shortcuts import get_current_site
except ImportError:
    from django.contrib.sites.models import get_current_site

class TeamListView(ListView):
    """
    A complete list of the personlist items
    """
    model = Person
    template_name = 'djangocms_personlist/team_index.html'
    filter_class = TeamMemberFilter

    def get_queryset(self):
        current_site = get_current_site(self.request)

        q = super(TeamListView, self).get_queryset()
        q = q.filter(active=True)
        q = q.filter(Q(sites=None)) | current_site.person_set.all()
        return self.filter_class(self.request.GET, q)

    def get_context_data(self, **kwargs):
        context = super(TeamListView, self).get_context_data(**kwargs)
        context['teams'] = Team.objects.filter(is_active=True)
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
    template_name = 'djangocms_personlist/person_detail.html'
    queryset = Person.objects.filter(active=True)
