# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import TeamListView, TeamDetailView, PersonListView, PersonDetailView

urlpatterns = patterns('',
    url(r'^(?P<pk>[\w-]+)/$',
        TeamDetailView.as_view(),
        name='team-detail'),
    url(r'^$',
        TeamListView.as_view(),
        name='team-list'),
    url(r'^person/(?P<pk>[\w-]+)/$',
        PersonDetailView.as_view(),
        name='person-detail'),
    url(r'^persons',
        PersonListView.as_view(),
        name='person-list'),
)
