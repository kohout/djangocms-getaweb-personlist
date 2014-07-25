# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import TeamIndexView, TeamListView, PersonDetailView

urlpatterns = patterns('',
    url(r'^team/(?P<pk>[\w-]+)/$',
        TeamListView.as_view(),
        name='team-list'),
    url(r'^person/(?P<pk>[\w-]+)/$',
        PersonDetailView.as_view(),
        name='person-detail'),
    url(r'^$',
        TeamIndexView.as_view(),
        name='team-index'),
)
