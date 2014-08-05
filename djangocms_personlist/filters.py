# -*- coding: utf-8 -*-
from django.db.models.query_utils import Q
from django_filters import FilterSet
from django_filters.filters import Filter
from djangocms_personlist.models import Person


def team_members(qs, value):
    terms = value.split(',')
    f = None
    for term in terms:
        if f is None:
            f = Q(teams__id=term)
        else:
            f = f |\
                Q(teams__id=term)

    return qs.filter(f)


class TeamMemberFilter(FilterSet):
    team = Filter(action=team_members)

    class Meta:
        model = Person
        fields = ['team']
