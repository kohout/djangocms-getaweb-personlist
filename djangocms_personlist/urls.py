# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import TeamListView, PersonDetailView

urlpatterns = patterns('',
    url(r'^person/(?P<pk>[\w-]+)/$',
        PersonDetailView.as_view(),
        name='person-detail'),
    url(r'^$',
        TeamListView.as_view(),
        name='team-index'),
)
