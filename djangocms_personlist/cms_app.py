from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from .menu import TeamsMenu


class TeamApp(CMSApp):
    name = _('Team Module')
    urls = ['djangocms_personlist.urls']
    app_name = 'cmsteam'
    menus = [TeamsMenu]

apphook_pool.register(TeamApp)
