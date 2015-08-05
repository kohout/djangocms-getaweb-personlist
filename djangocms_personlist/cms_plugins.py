from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import PersonListPluginModel, Person

try:
    # >= Django 1.7
    from django.contrib.sites.shortcuts import get_current_site
except ImportError:
    from django.contrib.sites.models import get_current_site

BASE_TEMPLATE_PATH = 'cms/plugins/personlist/'

class PersonListPlugin(CMSPluginBase):
    model = PersonListPluginModel
    name = _("Person List")
    render_template = '%sindex.html' % BASE_TEMPLATE_PATH

    def render(self, context, instance, placeholder):
        current_site = get_current_site(context['request'])

        context['instance'] = instance
        context['team'] = instance.selected_team
        context['persons'] = instance.get_persons(instance.selected_team, current_site)
        context['subtemplate'] = ''.join([BASE_TEMPLATE_PATH, instance.layout])
        return context

plugin_pool.register_plugin(PersonListPlugin)
