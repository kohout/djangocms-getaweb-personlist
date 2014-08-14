from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from djangocms_personlist.resolvers import reverse
from .models import Team


class TeamsMenu(CMSAttachMenu):

    name = _('Teams Menu')

    def get_nodes(self, request):
        nodes = []
        if not request.current_page:
            return nodes

        for team in Team.objects.all().order_by('name'):
            node = NavigationNode(
                team.name,
                team.get_absolute_url(),
                team.id,
                0,
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(TeamsMenu)
