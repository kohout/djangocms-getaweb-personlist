from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import PersonListPluginModel, Person

BASE_TEMPLATE_PATH = 'cms/plugins/personlist/'

class PersonListPlugin(CMSPluginBase):
    model = PersonListPluginModel
    name = _("Person List")
    render_template = '%sindex.html' % BASE_TEMPLATE_PATH

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['team'] = instance.selected_team
        context['persons'] = instance.selected_team.team_person.filter(active=True)
        context['subtemplate'] = ''.join([BASE_TEMPLATE_PATH, instance.layout])
        return context

plugin_pool.register_plugin(PersonListPlugin)
